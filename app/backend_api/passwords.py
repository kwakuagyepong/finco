from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController


def get_password():
    role = ["manager", "admin"]
    assigned_role = session['role']

    if assigned_role in role:
        required_fields = ['user_id'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        user_id = data['user_id']
        password = "Ghana"
        role_assigning = "teller"

        result_password = AuthenticationController.get_user_password(user_id,role_assigning,password)

        if result_password:
            return jsonify({'message': 'User registered successfully', 'status_code': 200}), 200
        else: 
            return jsonify({'error': 'Failed to add user', 'status_code': 500}), 500
        
    return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
