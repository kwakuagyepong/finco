from flask import Blueprint, jsonify, request, session
from app.models import users_of_credit_union, update_transaction

def get_approve_transaction():
    user_role = session['role']
    role_assigned = "manager"
    not_assigned = "Not Assigned"
    if user_role == role_assigned:

            user_id_session = session['user_id']
            # credit_id = session['credit_union_id']
            required_fields = ['transaction_ID']
            required_fields = ['CREDIT_UNION_ORIGINATING_ID']

            data = request.json
            # print("Incoming request data:", data) 
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            ORIGINATING_MANAGER_ID = data['ORIGINATING_MANAGER_ID']
            DESTINATION_MANAGER_ID = data['DESTINATION_MANAGER_ID']
            print("ORIGINATING_MANAGER_ID", ORIGINATING_MANAGER_ID)
            print("DESTINATION_MANAGER_ID", DESTINATION_MANAGER_ID)
            transaction_ID = data['transaction_ID']
            CREDIT_UNION_ORIGINATING_ID = data['CREDIT_UNION_ORIGINATING_ID']
            
            user_result = users_of_credit_union.get_users_of_credit_union(user_id_session)
            # print("Main Result", user_result)
            if user_result:
                credit_union_id = user_result[5]
                # print("credit_union_id", credit_union_id)
                if credit_union_id == CREDIT_UNION_ORIGINATING_ID:
                    if ORIGINATING_MANAGER_ID == not_assigned:
                        updated_transaction = update_transaction.get_update_transaction(user_id_session,transaction_ID)
                        print("ORIGINATING_MANAGER_ID", ORIGINATING_MANAGER_ID)
                        if updated_transaction:
                            return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                        else:
                            return jsonify({'error': 'Failed to Approve', 'status_code': 500}), 500
                    else:
                        return jsonify({'error': 'Transaction has already been approved', 'status_code': 501}), 501
                else:
                    if DESTINATION_MANAGER_ID == not_assigned:                                                                                                                           
                        updated_transaction1 = update_transaction.get_update_transaction_destination_manager(user_id_session,transaction_ID)
                        print("DESTINATION_MANAGER_ID", DESTINATION_MANAGER_ID)
                        if updated_transaction1:
                            return jsonify({'message': 'Transaction Approved', 'status_code': 200}), 200
                        else:
                            return jsonify({'error': 'Failed to Approve', 'status_code': 502}), 502
                    else: 
                        return jsonify({'error': 'Transaction has already been approved', 'status_code': 503}), 503 
                        
            return jsonify({'error': 'Result not found', 'status_code': 504}), 504

    return jsonify({'error': 'User is not a manager', 'status_code': 404}), 404

    