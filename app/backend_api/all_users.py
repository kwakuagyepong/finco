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



