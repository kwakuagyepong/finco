from .backend_api.create_user import add_user
from .backend_api.login_api import get_user
from .backend_api.logout_api import signout
from .backend_api.deposit import get_deposit
from .backend_api.disburse_funds import get_funds_data
from .backend_api.approve_transaction import get_approve_transaction
from .backend_api.credit_union import get_creditunion,get_all_creditunion
from .backend_api.transactions import get_all_transactions_teller,get_all_transactions_teller_pending

from flask import Blueprint, jsonify, request, session
# from app.controller import AuthenticationController

# from flask_cors import CORS


authentication_blueprint = Blueprint('users', __name__)
 
# CORS(authentication_blueprint) 


# New route to signup
@authentication_blueprint.route('/api/users', methods=['POST'])
def register_user():
    return add_user()
    
    
# Route to signin   
@authentication_blueprint.route('/api/users/<string:email>/<string:password>', methods=['GET'])
def signin_user(email, password):
    return get_user(email, password)


# Route to Signout 
@authentication_blueprint.route('/api/signout', methods=['POST'])
def logout():
    return signout()
    
    
 # Route to Insert transaction 
@authentication_blueprint.route('/api/deposit', methods=['POST']) 
def deposit_and_withdraw():
    return get_deposit()


@authentication_blueprint.route('/api/disbursefunds', methods=['GET'])
def get_funds():
    return get_funds_data()


@authentication_blueprint.route('/api/approve_transaction', methods=['POST'])
def approve_transaction():
    return get_approve_transaction()

<<<<<<< HEAD
            user_id_session = session['user_id']
            # credit_id = session['credit_union_id']
            required_fields = ['transaction_ID']
            required_fields = ['CREDIT_UNION_ORIGINATING_ID']

            data = request.json
            print("Incoming request data:", data) 
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            status = data['status']
            print("status", status)

            ORIGINATING_MANAGER_ID = data['ORIGINATING_MANAGER_ID']
            DESTINATION_MANAGER_ID = data['DESTINATION_MANAGER_ID']
            print("ORIGINATING_MANAGER_ID", ORIGINATING_MANAGER_ID)
            print("DESTINATION_MANAGER_ID", DESTINATION_MANAGER_ID)
            transaction_ID = data['transaction_ID']
            CREDIT_UNION_ORIGINATING_ID = data['CREDIT_UNION_ORIGINATING_ID']
            
            user_result = users_of_credit_union.get_users_of_credit_union(user_id_session)
            # print("Main Result", user_result)
            if user_result:
                credit_union_id = user_result[5]
                # print("credit_union_id", credit_union_id)
                if credit_union_id == CREDIT_UNION_ORIGINATING_ID:
                    if ORIGINATING_MANAGER_ID == not_assigned:
                        updated_transaction = update_transaction.get_update_transaction(user_id_session,transaction_ID)
                        print("ORIGINATING_MANAGER_ID", ORIGINATING_MANAGER_ID)
                        if updated_transaction:
                            return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                        else:
                            return jsonify({'error': 'Failed to Approve', 'status_code': 500}), 500
                    else:
                        return jsonify({'error': 'Transaction has already been approved', 'status_code': 501}), 501
                else:
                    if DESTINATION_MANAGER_ID == not_assigned:                                                                                                                           
                        updated_transaction1 = update_transaction.get_update_transaction_destination_manager(user_id_session,transaction_ID)
                        print("DESTINATION_MANAGER_ID", DESTINATION_MANAGER_ID)
                        if updated_transaction1:
                            return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                        else:
                            return jsonify({'error': 'Failed to Approve', 'status_code': 502}), 502
                    else: 
                        return jsonify({'error': 'Transaction has already been approved', 'status_code': 503}), 503 
                        
            return jsonify({'error': 'Result not found', 'status_code': 504}), 504

    return jsonify({'error': 'User is not a manager', 'status_code': 404}), 404

    

# Show all credit unions from transaction form (START)   
=======
# Credit Union short list on Teller Page (START)   
>>>>>>> 205ac7c9e1d9227b8edff93a48ce7e526b5a6164
@authentication_blueprint.route('/api/creditunions', methods=['GET']) 
def creditunion_short_display():
    return get_creditunion()   
    

# Show all credit Unions
@authentication_blueprint.route('/api/all_creditunions', methods=['GET']) 
def all_creditunion():
    return get_all_creditunion


# Show all transactions Viewed by Teller (START)
@authentication_blueprint.route('/api/all_transactions/teller', methods=['GET'])
def transactions_by_teller():
    return get_all_transactions_teller()



# Show all transactions Viewed by Teller on Transactions page(START)
@authentication_blueprint.route('/api/all_transactions_pending/teller', methods=['GET'])
def all_transactions():
    return get_all_transactions_teller_pending
            
