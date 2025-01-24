from flask import Blueprint, jsonify, session, request
from app.models import all_users


def get_all_teller():
    role = ["manager", "admin"]
    assigned_role = session['role']

    if assigned_role in role:

        credit_union_id = session['credit_union_id']
        user_id = session['user_id']

        result_users = all_users.get_all_users(credit_union_id,user_id)

        if result_users:
            formatted_result = [
                {
                    'result': {
                        'credit_union_user_id' : row[0],
                        'first_name': row[1],
                        'last_name' : row[2],
                        'email' : row[3],
                        'phone_number': row[4],
                        'status': row[6]
                    },
                }
                for row in result_users
            ]
            return jsonify(formatted_result)
        else: 
            return jsonify({'error': 'No Users Found', 'status_code': 404}), 404
    return jsonify({'error': 'Unauthorized access', 'status_code': 404}), 404


def get_update_users():
    role = ["manager", "admin", "teller"]
    assigned_role = session['role']

    if assigned_role in role:

        required_fields = ['credit_union_user_id', 'first_name', 'last_name', 'email', 'phone_number', 'status'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        credit_union_user_id = data['credit_union_user_id']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone_number = data['phone_number']
        status = data['status']

        result_users = all_users.update_user(credit_union_user_id,first_name, last_name, email, phone_number, status)

        if result_users:
                return jsonify({'message': 'User updated successfully','status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to update user', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
