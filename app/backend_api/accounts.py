from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController
from app.models import accounts



def assign_password():
    assigned_role = session['role']

    if assigned_role == "manager":
        required_fields = ['transaction_ID'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
    
# Get Credit Union current account data
def account_data():
    role = ["teller","manager","admin"]
    assigned_role = session['role']

    if assigned_role in role:
        results = accounts.get_credit_union_accounts()
        if results:

            formatted = [
                {
                    'results': {
                        'id': row[0], 
                        'amount': row[1],
                        'credit_union_id': row[2],
                        'credit_union_name': row[4]
                    },
                    'status_code': 200
                }
                for row in results
            ]
            return jsonify(formatted),200    
        else:
            return jsonify({'error': 'Credit Union account data not found', 'status_code': 404}),   
                
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
# Get Credit Union current account data END    

# Get Credit Union account data deposit history
def account_data_deposit_history():
    assigned_role = session['role']
    if assigned_role in "manager":
        results = accounts.get_accounts_deposite_history()
        if results:

            formatted = [
                {
                    'results': {
                        'id': row[0], 
                        'amount': row[1],
                        'credit_union_id': row[2],
                        'user_id': row[3],
                        'date': row[4]
                    },
                    'status_code': 200
                }
                for row in results
            ]
            return jsonify(formatted),200    
        else:
            return jsonify({'error': 'Credit Union account history not found', 'status_code': 404}),   
                
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
    



