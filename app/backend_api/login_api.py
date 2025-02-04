from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController

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
                    'id': user[0],
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