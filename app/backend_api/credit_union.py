from flask import Blueprint, jsonify, session, request
from app.models import CreditUnionmodel,all_CreditUnionmodels,Admin_use


def get_creditunion():
    results = CreditUnionmodel.get_credit_unions()

    if results:
        
        formatted = [
            {
                'results': {
                      'id': row[0], 
                      'Credit Union': row[1],
                      'address': row[2], 
                      'address_2': row[3], 
                      'Phone Number': row[4], 
                      'Email': row[5],
                },
                 'status_code': 200
            }
            for row in results
        ]
        return jsonify(formatted),200
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
    

def get_all_creditunion():
    results = all_CreditUnionmodels.get_all_credit_unions()

    if results:
        
        formatted = [
            {
                'results': {
                      'id': row[0], 
                      'Credit Union': row[1],
<<<<<<< HEAD
                      'Location': row[2], 
                      'Location_2': row[3],
=======
                      'address': row[2], 
                      'address_2': row[3],
>>>>>>> 962d9c1d14beb0f47c004430cb321c239dd3bb60
                      'Phone Number': row[4], 
                      'Email': row[5]
                },
                 'status_code': 200
            }
            for row in results
        ]
        return jsonify(formatted),200
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
    
# Register a new Credit Union with Admin role
def register_creditunion():
    role = "admin"
    assigned_role = session['role']

    if assigned_role == role:
            required_fields = ['Credit_Union', 'address','address_2', 'phone_number', 'email'] 
            data = request.json
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            Credit_Union = data['Credit_Union']
            address = data['address']
            address_2 = data['address_2']
            phone_number = data['phone_number']
            email = data['email']
            status = "disabled"

            credit_union = all_CreditUnionmodels.register_the_creditunion(Credit_Union,address,address_2,phone_number,email,status)
            if credit_union:
                return jsonify({'message': 'Credit Union registered successfully','status_code': 200}), 200
            else:
                return jsonify({'error': 'Failed to register', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400

def update_creditunion_status():
    role = "admin"
    assigned_role = session['role']

    if assigned_role == role:
        required_fields = ['Credit_Union_id', 'status'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        Credit_Union_id = data['Credit_Union_id']
        status = data['status']

        credit_union = Admin_use.updated_credit_union_status(Credit_Union_id,status)
        if credit_union:
            return jsonify({'message': 'Status updated successfully','status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to update', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400

# Update the creditunion information with Admin role
# This function is used to update the credit union information by the admin role
def update_credit_union_information():
    role = "admin"
    assigned_role = session['role']

    if assigned_role == role:
        required_fields = ['Credit_Union_id', 'Credit_Union_name', 'address', 'address_2','phone_number', 'email'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        Credit_Union_id = data['Credit_Union_id']
        Credit_Union = data['Credit_Union_name']
        address = data['address']
        address_2 = data['address_2']
        phone_number = data['phone_number']
        email = data['email']

        credit_union = Admin_use.update_credit_union_data(Credit_Union_id,Credit_Union,address,address_2,phone_number,email)
        if credit_union:
            return jsonify({'message': 'Credit Union updated successfully','status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to update', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400


    




        
            
            