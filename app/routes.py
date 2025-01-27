from .backend_api.create_user import add_user, get_update_users
from .backend_api.login_api import get_user
from .backend_api.logout_api import signout
from .backend_api.deposit import get_deposit
from .backend_api.disburse_funds import get_funds_data
from .backend_api.approve_transaction import get_approve_transaction
from .backend_api.credit_union import get_creditunion,get_all_creditunion,register_creditunion
from .backend_api.transactions import get_all_transactions_teller,get_all_transactions_teller_pending
<<<<<<< HEAD
from .backend_api.passwords import get_password
from .backend_api.all_users import get_all_teller
=======
from .backend_api.passwords import get_password,update_passowrd
from .backend_api.all_users import get_all_teller,get_update_users
>>>>>>> a26871bb36a6eda08e3129004fedc985906cdc5e


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


# Show all credit unions from transaction form (START)   
@authentication_blueprint.route('/api/creditunions', methods=['GET']) 
def creditunion_short_display():
    return get_creditunion()   
    

# Show all credit Unions
@authentication_blueprint.route('/api/all_creditunions', methods=['GET']) 
def all_creditunion():
    return get_all_creditunion()


# Add a credit Union
@authentication_blueprint.route('/api/add_credit_union', methods=['POST']) 
def add_a_credit_union():
    return register_creditunion()


# Show all transactions Viewed by Teller (START)
@authentication_blueprint.route('/api/all_transactions/teller', methods=['GET'])
def transactions_by_teller():
    return get_all_transactions_teller()



# Show all transactions Viewed by Teller on Transactions page(START)
@authentication_blueprint.route('/api/all_transactions_pending/teller', methods=['GET'])
def all_transactions():
    return get_all_transactions_teller_pending()


@authentication_blueprint.route('/api/assign_password', methods=['POST'])
def password_get():
    return get_password()

@authentication_blueprint.route('/api/get_all_tellers', methods=['GET'])
def user_all():
    return get_all_teller()    

@authentication_blueprint.route('/api/update_user', methods=['POST'])
def update_user_all():
    return get_update_users()


@authentication_blueprint.route('/api/change_password', methods=['POST'])
def change_password():
    return update_passowrd()


