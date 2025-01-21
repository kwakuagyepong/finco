from flask import Blueprint, jsonify, request, session
from app.models import disbursingfunds

def get_funds_data():
    required_fields = ['transaction_ID'] 
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    transaction_ID = data['transaction_ID']
    full_data = disbursingfunds.get_funds_transaction(transaction_ID)

    if full_data:
        ORIGINATING_MANAGER_ID = [12]
        DESTINATION_MANAGER_ID = [13]

        if not ORIGINATING_MANAGER_ID or not DESTINATION_MANAGER_ID:
            return jsonify({
                'error': 'error releasing funds. Transaction has not being approved',
                'status_code': 400
            }), 400    

        # If both IDs are present, proceed with the response
        return jsonify({'data': full_data, 'status_code': 200}), 200
    
    return jsonify({'error': 'Transaction not found.', 'status_code': 404}), 404