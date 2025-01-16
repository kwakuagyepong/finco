from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController
from datetime import datetime
# from flask_cors import CORS
from app.models import CreditUnionmodel, all_transactions_teller, all_transaction_inbound, CreditUnion_deposit, all_transactions_on_transations_page_teller, disbursingfunds, users_of_credit_union, update_transaction

authentication_blueprint = Blueprint('users', __name__)
 
# CORS(authentication_blueprint) 




# New route to signup
@authentication_blueprint.route('/api/users', methods=['POST'])
def add_user():
    required_fields = ['email', 'password'] 
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
     
    email = data['email']
    password = data['password']

    # Call controller method to signup
    new_user = AuthenticationController.add_user(email, password)
    
    if new_user:
        return jsonify({'message': 'User registered successfully', 'user': new_user, 'status_code': 200}), 200
    else:
        return jsonify({'error': 'Failed to add user', 'status_code': 500}), 500
    
    
# Route to signin   
@authentication_blueprint.route('/api/users/<string:email>/<string:password>', methods=['GET'])
def get_user(email, password):
    user = AuthenticationController.get_user(email, password)
    
    if user:
        if user[6] == 'inactive':
            return jsonify({'error': 'User is Inactive', 'status_code': 402}), 402

        # create a session for the credit union ID and ID for Teller name
        session['credit_union_id'] = user[4]
        session['user_id'] = user[2]
        session['role'] = user[1]

        
        if user[1] in ['admin', 'manager', 'teller']:
            return jsonify({
                'user': 
                {
                    # 'id': user[0],
                    'credit_union_id': user[4],
                    'email': user[3],
                    'role': user[1],
                    'first_name': user[5],
                    'user_id': user[2],
                    'status': user[6]
                    
                },'status_code': 200}), 200
        else:
            return jsonify({'error': 'User role not assigned', 'status_code': 403}), 403

    else:
        return jsonify({'error': 'Wrong email or password', 'status_code': 404}), 404
       
# Route to Signout 
@authentication_blueprint.route('/api/signout', methods=['POST'])
def signout():
    # Remove the user from session
    session.pop('credit_union_id', None)  # Remove the credit_union_id
    session.pop('user_id', None)  # Remove the user_id
    return jsonify({'Message': 'User not found', 'status_code': 200}), 200

    
 # Route to Insert transaction 
@authentication_blueprint.route('/api/deposit', methods=['POST']) 
def get_deposit():
    # Get data on transactions
     if 'user_id' in session:
        user_id_session = session['user_id']
        credit_union_originating_id_number = session['credit_union_id']
        print('This is the session', credit_union_originating_id_number)

        deposit_result = ['first_name', 'last_name', 'transaction_type', 'amount', 'account_number', 'customer_id_number', 'customer_id_image', 'credit_union_destination_id']
        data = request.json
        missing_fields = [field for field in deposit_result if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code':400}),400
        
        first_name = data['first_name']
        last_name = data['last_name']
        transaction_type = data['transaction_type']
        amount = data['amount']
        account_number = data['account_number']
        customer_id_number = data['customer_id_number']
        customer_id_image = data['customer_id_image']
        credit_union_destination_id = data['credit_union_destination_id']
        credit_union_originating_id = credit_union_originating_id_number
        teller_name_id = user_id_session
        date = datetime.now().date()
        
        print('destination id', credit_union_destination_id)
        full_transaction = CreditUnion_deposit.push_transaction_desopit(first_name, last_name, transaction_type, amount, account_number, customer_id_number, customer_id_image, credit_union_destination_id, credit_union_originating_id, teller_name_id, date)

        if full_transaction:
            return jsonify({'message': 'Transaction submitted', 'status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to submit', 'status_code': 500}), 500
        
 


     else:
         return jsonify({'Error': 'User ID not found to initialize transaction'})


@authentication_blueprint.route('/api/disbursefunds', methods=['GET'])
def get_funds_data():
    required_fields = ['transaction_ID'] 
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    transaction_ID = data['transaction_ID']
    full_data = disbursingfunds.get_funds_transaction(transaction_ID)

    if full_data:
        ORIGINATING_MANAGER_ID = full_data.get('ORIGINATING_MANAGER_ID')
        DESTINATION_MANAGER_ID = full_data.get('DESTINATION_MANAGER_ID')

        if not ORIGINATING_MANAGER_ID or not DESTINATION_MANAGER_ID:
            return jsonify({
                'error': 'error releasing funds. Transaction has not being approved',
                'status_code': 400
            }), 400    

        # If both IDs are present, proceed with the response
        return jsonify({'data': full_data, 'status_code': 200}), 200
    
    return jsonify({'error': 'Transaction not found.', 'status_code': 404}), 404


@authentication_blueprint.route('/api/approve_transaction', methods=['POST'])
def get_approve_transaction():
    user_role = session['role']
    role_assigned = "manager"
    if user_role == role_assigned:

            user_id_session = session['user_id']
            
            # credit_id = session['credit_union_id']

            required_fields = ['transaction_ID']
            required_fields = ['CREDIT_UNION_ORIGINATING_ID']
             
            data = request.json
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            transaction_ID = data['transaction_ID']
            CREDIT_UNION_ORIGINATING_ID = data['CREDIT_UNION_ORIGINATING_ID']
            user_result = users_of_credit_union.get_users_of_credit_union(user_id_session)

            if user_result:
                credit_union_id = user_result.get('credit_union_id')

                if credit_union_id == CREDIT_UNION_ORIGINATING_ID:
                    updated_transaction = update_transaction.get_update_transaction(user_id_session,transaction_ID)
                    if updated_transaction:
                        return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                    else:
                        return jsonify({'error': 'Failed to Approve', 'status_code': 500}), 500
                else: 
                    updated_transaction1 = update_transaction.get_update_transaction(user_id_session,transaction_ID)
                    if updated_transaction1:
                        return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                    else:
                        return jsonify({'error': 'Failed to Approve', 'status_code': 500}), 500
            return  

    return jsonify({'error': 'User is not a manager', 'status_code': 404}), 404

    

# Show all credit unions from transaction form (START)   
@authentication_blueprint.route('/api/creditunions', methods=['GET']) 
def get_creditunion():
    results = CreditUnionmodel.get_credit_unions()

    if results:
        
        formatted = [
            {
                'results': {
                      'id': row[0], 
                      'Credit Union': row[1],
                      'Location': row[2], 
                      'Phone Number': row[3], 
                      'Email': row[4],
                },
                 'status_code': 200
            }
            for row in results
        ]
        return jsonify(formatted),200
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
# Show all credit unions from transaction form (END)     
    

# Show all credit unions on Credit Unions page (Currently by Teller page) (Start) 
# @authentication_blueprint.route('/api/all_creditunions', methods=['GET']) 
# def get_creditunion():
#     results = CreditUnionmodel.get_credit_unions()

#     if results:
        
#         formatted = [
#             {
#                 'results': {
#                       'id': row[0], 
#                       'Credit Union': row[1],
#                       'Location': row[2], 
#                       'Phone Number': row[3], 
#                       'Email': row[4]
#                 },
#                  'status_code': 200
#             }
#             for row in results
#         ]
#         return jsonify(formatted),200
#     else:
#         return jsonify({'error': 'User not found', 'status_code': 404}), 404

# Show all credit unions on Credit Unions page (Currently by Teller page) (END) 

# Show all transactions Viewed by Teller (START)
@authentication_blueprint.route('/api/all_transactions/teller', methods=['GET'])
def get_all_transactions_teller():
    if 'teller' in session:
        credit_union_id = session['credit_union_id']
        # teller = session['teller']
        print(credit_union_id)

        transactions = all_transactions_teller.get_transactions_all_teller(credit_union_id)

        if transactions:
            formatted_transaction = [
                { 
                    'result': {
                        'AMOUNT' : row[4],
                        'CREDIT_UNION_DESTINATION_ID': row[5],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'TIMESTAMP': row[6],
                        'TRANSACTION_ID': row[0],
                        'TRANSACTION_TYPE' : row[3]
                    },
                    'status_code': 200
                }
                for row in transactions
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'No Transactions found', 'status_code': 404}), 404
# Show all transactions Viewed by Teller (END)

# Show all transactions Viewed by Teller on Transactions page(START)
@authentication_blueprint.route('/api/all_transactions_pending/teller', methods=['GET'])
def get_all_transactions_teller_pending():
    if 'teller' in session:
        credit_union_id = session['credit_union_id']
        credit_union_id_repeat = credit_union_id
        

        # Fetch transactions
        transactions_results = all_transactions_on_transations_page_teller.all_transactions_transactions_page_by_teller(credit_union_id,credit_union_id_repeat)
        print('Before edit', transactions_results)
        
        if transactions_results:
            formatted_transaction = [
                {   
                    'result': {
                        'AMOUNT' : row[4],
                        'CREDIT_UNION_DESTINATION_ID': row[8],
                        'CREDIT_UNION_ORIGINATING_ID': row[9],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'ACCOUNT_NUMBER' : row[5],
                        'CUSTOMER_ID' : row[6],
                        'TIMESTAMP': row[13],
                        'TRANSACTION_ID': row[0],
                        'TRANSACTION_TYPE' : row[3],
                        'ORIGINATING_MANAGER_ID': row[15],
                        'DESTINATION_MANAGER_ID': row[16],
                        'STATUS' : row[17]
                    },
                    'status_code': 200
                }
                for row in transactions_results
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'No Transactions found', 'status_code': 404}), 404
            
    return jsonify({'error': 'User not Found', 'status_code': 404}), 404
            
# Show all transactions pending Viewed by Teller Dashboard (END)



# @authentication_blueprint.route('/api/all_transactions', methods=['GET'])
# def get_all_transactions():
#     if 'credit_union_id' in session:
#         credit_union_id = session['credit_union_id']

#         transactions = all_transactions.get_transactions_all(credit_union_id)

#         if transactions:
#             formatted_transaction = [
#                 {
#                     'result': {
#                         'TRANSACTION_ID': row[0],
#                         'CUSTOMER_FIRST_NAME' : row[1],
#                         'CUSTOMER_LAST_NAME' : row[2],
#                         'TRANSACTION_TYPE' : row[3],
#                         'AMOUNT' : row[4],

#                     },
#                     'status_code': 200
#                 }
#                 for row in transactions
#             ]
#             return jsonify(formatted_transaction),200
#         else:
#             return jsonify({'error': 'User not found', 'status_code': 404}), 404



# @authentication_blueprint.route('/api/all_inbound', methods=['GET'])
# def get_all_inbound_transactions():
#     if 'credit_union_id' in session:
#         credit_union_id = session['credit_union_id']

#         transactions_inbound = all_transaction_inbound.get_inbound_transactions_all(credit_union_id)

#         if transactions_inbound:
#             formatted_transaction = [
#                 {
#                     'result': {
#                         'TRANSACTION_ID': row[0],
#                         'CUSTOMER_FIRST_NAME' : row[1],
#                         'CUSTOMER_LAST_NAME' : row[2],
#                         'TRANSACTION_TYPE' : row[3],
#                         'AMOUNT' : row[4],

#                     },
#                     'status_code': 200
#                 }
#                 for row in transactions_inbound
#             ]
#             return jsonify(formatted_transaction),200
#         else:
#             return jsonify({'error': 'User not found', 'status_code': 404}), 404
        

