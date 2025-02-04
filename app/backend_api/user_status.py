from flask import jsonify, request, session
from app.models import user_status

def assign_user_status():
    role = ["manager", "admin"]
    assigned_role = session['role']

    if assigned_role in role:
        required_fields = ['user_id','status'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        user_id = data['user_id']
        user_status_current = data['status']

        result_status = user_status.get_status(user_id,user_status_current)

        if result_status:
            return jsonify({'message': 'Status updated successfully','status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to updated Status', 'status_code': 400}), 400
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400





        