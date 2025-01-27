from flask import Blueprint, jsonify, session, request
from app.models import CreditUnionmodel,all_CreditUnionmodels


def get_creditunion():
    results = CreditUnionmodel.get_credit_unions()

    if results:
        
        formatted = [
            {
                'results': {
                      'id': row[0], 
                      'Credit Union': row[1],
                      'Location': row[2], 
                      'Phone Number': row[3], 
                      'Email': row[4],
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
                      'Location': row[2], 
                      'Phone Number': row[3], 
                      'Email': row[4]
                },
                 'status_code': 200
            }
            for row in results
        ]
        return jsonify(formatted),200
    else:
        return jsonify({'error': 'User not found', 'status_code': 404}), 404
    

def register_creditunion():
    role = "admin"
    assigned_role = session['role']

    if assigned_role == role:
            required_fields = ['Credit_Union', 'address', 'phone_number', 'email'] 
            data = request.json
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                error_message = f"Missing fields: {', '.join(missing_fields)}"
                return jsonify({'error': error_message, 'status_code': 400}), 400
            
            Credit_Union = data['Credit_Union']
            address = data['address']
            phone_number = data['phone_number']
            email = data['email']
            status = "disabled"

            credit_union = all_CreditUnionmodels.register_the_creditunion(Credit_Union,address,phone_number,email,status)
            if credit_union:
                return jsonify({'message': 'Credit Union registered successfully','status_code': 200}), 200
            else:
                return jsonify({'error': 'Failed to register', 'status_code': 500}), 500
    else:
        return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
    




        
            
            