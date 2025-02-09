from flask import Blueprint, jsonify, session, request
from app.models import Admin_use

def add_user_manager():
    role = "admin"
    assigned_role = session['role']

    if assigned_role == role:
            required_fields = ['credit_Union_id', 'users_id'] 
            data = request.json
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            credit_Union = data['credit_Union_id']
            users_id = data['users_id']
            role = "manager"

            checking_if_exist = Admin_use.check_existing_user(users_id)
            if checking_if_exist:
                return jsonify({'message': 'User has already been assigned as a Manager','status_code': 400}), 400
            else:
                credit_union = Admin_use.set_manager(credit_Union,users_id,role)
                if credit_union:
                    return jsonify({'message': 'Updated successfully','status_code': 200}), 200
                else:
                    return jsonify({'error': 'Failed to Update', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
    

def get_all_managers():
        role = "admin"
        assigned_role = session['role']

        if assigned_role == role:
            results = Admin_use.all_credit_union_managers()

            if results:
                
                formatted = [
                    {
                        'results': {
                            'id': row[0], 
                            'CREDIT_UNION': row[1],
                            'MANAGER_ID': row[2]
                        },
                        'status_code': 200
                    }
                    for row in results
                ]
                return jsonify(formatted),200
            else:
                return jsonify({'error': 'User not found', 'status_code': 404}), 404
        else:
            return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400

def get_credit_union_managers():
    role = ["teller","manager","admin"]
    assigned_role = session['role']

    if assigned_role in role:
            results = Admin_use.view_manager_information()

            if results:
                
                formatted = [
                    {
                        'results': {
                            'manager_id': row[0], 
                            'first_name': row[1],
                            'last_name': row[2],
                            'user_status': row[3], 
                            'credit_union_name': row[4],
                            'address': row[5],
                            'credit_union_id': row[6],
                            'phone_number': row[7],
                            'credit_union_status': row[8],
                            'credit_union_email': row[9]
                        },
                        'status_code': 200
                    }
                    for row in results
                ]
                return jsonify(formatted),200
            else:
                return jsonify({'error': 'User not found', 'status_code': 404}), 404
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
        





