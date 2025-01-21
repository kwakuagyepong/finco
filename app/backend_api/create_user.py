from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController


# New route to signup
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