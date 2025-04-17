from flask import Blueprint, jsonify, request, session
from app.models import CreditUnion_deposit,Admin_use
from datetime import datetime
from PIL import Image 
import base64
import os
from io import BytesIO
import os


def get_deposit():
    # Get data on transactions
     if 'user_id' in session:
        user_id_session = session['user_id']
        credit_union_originating_id_number = session['credit_union_id']
        print('This is the session', credit_union_originating_id_number)

        deposit_result = ['first_name', 'last_name', 'transaction_type', 'amount', 'account_number', 'customer_id_number', 'customer_id_image', 'credit_union_destination_id']
        data = request.json
        missing_fields = [field for field in deposit_result if field not in data]
        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code':400}),400
        
        first_name = data['first_name']
        last_name = data['last_name']
        transaction_type = data['transaction_type']
        amount = data['amount']
        account_number = data['account_number']
        customer_id_number = data['customer_id_number']
        customer_id_image = data['customer_id_image']
        credit_union_destination_id = data['credit_union_destination_id']
        credit_union_originating_id = credit_union_originating_id_number
        teller_name_id = user_id_session
        date = datetime.now().date()

        #Save the customer ID image 

        # directory of image
        UPLOAD_FOLDER = 'customer_id_cards'

        # Create the directory if it doesn't exist
        #if not os.path.exists(UPLOAD_FOLDER):
            #os.makedirs(UPLOAD_FOLDER)

        try:
            # Decode the base64 image
            image_data = base64.b64decode(customer_id_image)
            image = Image.open(BytesIO(image_data))
            filename = f"{UPLOAD_FOLDER}/{customer_id_number}_{first_name}_{last_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            filenamedb = f"{customer_id_number}_{first_name}_{last_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            image.save(filename)
            print(f"Image saved to {filename}")
        except Exception as e:
            print(f"Failed to save image: {e}")
            return jsonify({'error': 'Failed to save customer ID image', 'status_code': 500}), 500

        # Get the cap amount for the originating credit union
        check_amount_cap = Admin_use.get_cap_amount(credit_union_originating_id)
        capped_amount = check_amount_cap[1]
        print("CUP Amount", capped_amount)
        # If the amount is below the cap amount, bypass the originating manager approval
        if amount <= capped_amount:
            originating_manager_id = "SYSTEM"
        else:
            originating_manager_id = ""
        # print('destination id', credit_union_destination_id)
        full_transaction = CreditUnion_deposit.push_transaction_desopit(first_name, last_name, transaction_type, amount, account_number, customer_id_number, filenamedb, credit_union_destination_id, credit_union_originating_id, teller_name_id, date,originating_manager_id)

        if full_transaction:
            return jsonify({'message': 'Transaction submitted', 'status_code': 200}), 200
        else:
            return jsonify({'error': 'Failed to submit', 'status_code': 500}), 500

     else:
         return jsonify({'Error': 'User ID not found to initialize transaction'})
