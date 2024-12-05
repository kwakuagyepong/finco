from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController
# from flask_cors import CORS
from app.models import CreditUnionmodel, all_transactions, all_transaction_inbound

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
        if user[5] == 'inactive':
            return jsonify({'error': 'User is Inactive', 'status_ code': 402}), 402

        # create a session for the credit union name
        session['credit_union_name'] = user[3]
        
        if user[1] in ['admin', 'manager', 'teller']:
            return jsonify({
                'user': 
                {
                    'id': user[0],
                    'Credit Union': user[3],
                    'email': user[2],
                    'role': user[1],
                    'first_name': user[4],
                    'status': user[5]
                },'status_code': 200}), 200
        else:
            return jsonify({'error': 'User role not assigned', 'status_code': 403}), 403

    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
    
    
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
                      'Status': row[5]
                },
                 'status_code': 200
            }
            for row in results
        ]
        return jsonify(formatted),200
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
    


@authentication_blueprint.route('/api/all_transactions', methods=['GET'])
def get_all_transactions():
    if 'credit_union_name' in session:
        credit_union_id = session['credit_union_name']

        transactions = all_transactions.get_transactions_all(credit_union_id)

        if transactions:
            formatted_transaction = [
                {
                    'result': {
                        'TRANSACTION_ID': row[0],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'TRANSACTION_TYPE' : row[3],
                        'AMOUNT' : row[4],

                    },
                    'status_code': 200
                }
                for row in transactions
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'User not found', 'status_code': 404}), 404



@authentication_blueprint.route('/api/all_inbound', methods=['GET'])
def get_all_inbound_transactions():
    if 'credit_union_name' in session:
        credit_union_id = session['credit_union_name']

        transactions_inbound = all_transaction_inbound.get_inbound_transactions_all(credit_union_id)

        if transactions_inbound:
            formatted_transaction = [
                {
                    'result': {
                        'TRANSACTION_ID': row[0],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'TRANSACTION_TYPE' : row[3],
                        'AMOUNT' : row[4],

                    },
                    'status_code': 200
                }
                for row in transactions_inbound
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'User not found', 'status_code': 404}), 404
        

