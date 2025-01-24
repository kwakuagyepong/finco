from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController
from app.models import add_a_user


# New route to signup
def add_user():
    role = ["manager", "admin"]
    assigned_role = session['role']
    
    if assigned_role in role:
            required_fields = ['first_name', 'last_name', 'email', 'phone_number'] 
            data = request.json
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            phone_number = data['phone_number']
            status = "inactive"
            credit_union = session['credit_union_id']

            # Call controller method to signup
            new_user = add_a_user.add_new_user(first_name, last_name, email, phone_number, credit_union, status)
            
            if new_user:
                return jsonify({'message': 'User registered successfully', 'user': new_user, 'status_code': 200}), 200
            else:
                return jsonify({'error': 'Failed to add user', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400