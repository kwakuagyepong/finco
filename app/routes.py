from .backend_api.create_user import add_user, get_update_users, create_new_user_by_admin
from .backend_api.login_api import get_user
from .backend_api.logout_api import signout
from .backend_api.deposit import get_deposit
from .backend_api.disburse_funds import get_disburse_funds
from .backend_api.approve_transaction import get_approve_transaction
from .backend_api.credit_union import get_creditunion,get_all_creditunion,register_creditunion
from .backend_api.transactions import get_all_transactions_teller,get_all_transactions_teller_pending,get_all_transactions_statements
from .backend_api.passwords import assign_password,update_password
from .backend_api.all_users import get_all_teller
from .backend_api.user_status import assign_user_status
from .backend_api.admin_functions import get_users
from .backend_api.managers import add_user_manager, get_all_managers,get_credit_union_managers
from .backend_api.accounts import account_data,account_data_deposit_history,account_data_deposit_history_specific_credit_union


from flask import Blueprint, jsonify, request, session
# from app.controller import AuthenticationController

#from flask_cors import CORS


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


@authentication_blueprint.route('/api/disbursefunds', methods=['POST'])
def get_funds():
    return get_disburse_funds()


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



# Show all transactions not disbursed on Transactions page 
@authentication_blueprint.route('/api/all_transactions_pending/teller', methods=['GET'])
def all_transactions():
    return get_all_transactions_teller_pending()


# Show all transactions disbursed on statement page 
@authentication_blueprint.route('/api/transactions_statements', methods=['GET'])
def all_transactions_statement():
    return get_all_transactions_statements()


@authentication_blueprint.route('/api/assign_password', methods=['POST'])
def password_get():
    return assign_password()

@authentication_blueprint.route('/api/get_all_tellers', methods=['GET'])
def user_all():
    return get_all_teller()    


@authentication_blueprint.route('/api/update_user', methods=['POST'])
def update_user_all():
    return get_update_users()


@authentication_blueprint.route('/api/change_password', methods=['POST'])
def change_password():
    return update_password()
 
    
# Update status of credit union
@authentication_blueprint.route('/api/set_user_status', methods=['POST'])
def get_status():
    return assign_user_status()


# View all users
@authentication_blueprint.route('/api/get_users_all', methods=['GET'])
def get_all_users():
    return get_users()

# Create new user by administrator
@authentication_blueprint.route('/api/create_user_done_by_admin', methods=['GET'])
def create_user_administrator():
    return create_new_user_by_admin()


# Assign a Manager by Admin
@authentication_blueprint.route('/api/assign_a_manager', methods=['POST'])
def assign_manager():
    return add_user_manager()

# Assign a Manager by Admin
@authentication_blueprint.route('/api/get_all_credit_union_managers', methods=['GET'])
def view_managers():
    return get_all_managers()


# Manager information with inner join credit union information and user information
@authentication_blueprint.route('/api/credit_union_info_with_manager', methods=['GET'])
def info_managers_credit_union():
    return get_credit_union_managers()


# Get all Credit Union account data
@authentication_blueprint.route('/api/credit_union_account_access', methods=['GET'])
def get_credit_union_account():
    return account_data()


# Get all Credit Union accounts data deposit history (Supper Admin)
@authentication_blueprint.route('/api/all_account_deposit_history', methods=['GET'])
def get_all_account_deposit_history():
    return account_data_deposit_history()


# Get specific Credit Union accounts data deposit history
@authentication_blueprint.route('/api/specific_account_deposit_history', methods=['GET'])
def get_specific_account_deposit_history():
    return account_data_deposit_history_specific_credit_union()