from flask import Blueprint, jsonify
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