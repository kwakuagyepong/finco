from flask import Blueprint, jsonify, request, session
from app.controller import AuthenticationController
from app.models import checks



def assign_password():
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
        # check of there is data in the credencials_id.
        try:
            credentials_id = data['credencials_id']
        except KeyError:
            credentials_id = None  # Assign.
        users_password = "Ghana"
        role_assigning = "teller"
 
        get_data = checks.check_for_data_for_credentials_tables(user_id)
        # print(get_data)
        if get_data: 
            the_credentials = get_data[0]
            # print("The user Id", the_credentials)
            result_password = AuthenticationController.change_user_password(the_credentials,users_password)
        else:
            result_password = AuthenticationController.get_user_password(user_id,role_assigning,users_password) 
        if result_password:
            return jsonify({'message': 'Password successfully updated', 'status_code': 200}), 200
        else: 
            return jsonify({'error': 'Failed to process password', 'status_code': 500}), 500
        
    return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400


def update_password():
    role = ["manager", "admin", "teller"]
    assigned_role = session['role']

    if assigned_role in role:
        required_fields = ['credencials_id', 'users_password'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        credentials_id = data['credencials_id']
        users_password = data['users_password']

        result_password = AuthenticationController.change_user_password(credentials_id,users_password)

        if result_password:
            return jsonify({'message': 'Password updated successfully','status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to updated password', 'status_code': 400}), 400
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400





 