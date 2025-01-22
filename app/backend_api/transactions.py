from flask import Blueprint, jsonify, session, send_from_directory
from app.models import all_transactions_teller,all_transactions_on_transations_page_teller
import os
from io import BytesIO
from PIL import Image
from datetime import datetime
import base64
 
UPLOAD_FOLDER = 'customer_id_cards'

def get_all_transactions_teller():
    assigned_role = session['role']
    role = "teller"
    print("User Role", assigned_role)

    if assigned_role == role:
        credit_union_id = session['credit_union_id']
        # teller = session['teller']
        # print(credit_union_id)

        transactions = all_transactions_teller.get_transactions_all_teller(credit_union_id)

        if transactions:
            formatted_transaction = [
                { 
                    'result': {
                        'AMOUNT' : row[4],
                        'CREDIT_UNION_DESTINATION_ID': row[5],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'TIMESTAMP': row[6],
                        'TRANSACTION_ID': row[0],
                        'TRANSACTION_TYPE' : row[3]
                    },
                    'status_code': 200
                }
                for row in transactions
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'No Transactions found', 'status_code': 404}), 404
    return jsonify({'error': 'Only teller can access this', 'status_code': 404}), 404
        


def get_all_transactions_teller_pending():
    role = ["teller", "manager", "admin"]
    assigned_role = session['role']

    if assigned_role in role:
        credit_union_id = session['credit_union_id']
        credit_union_id_repeat = credit_union_id
        

        # Fetch transactions
        transactions_results = all_transactions_on_transations_page_teller.all_transactions_transactions_page_by_teller(credit_union_id,credit_union_id_repeat)
        # print('Before edit', transactions_results)
        
        if transactions_results:
            formatted_transaction = [
                {   
                    'result': {
                        'AMOUNT' : row[4],
                        'CREDIT_UNION_DESTINATION_ID': row[8],
                        'CREDIT_UNION_ORIGINATING_ID': row[9],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'ACCOUNT_NUMBER' : row[5],
                        'CUSTOMER_ID' : row[6],
                        'CUSTOMER_ID_CARD_IMAGE' : get_image_base64(row[7]),
                        'TIMESTAMP': row[13],
                        'TRANSACTION_ID': row[0],
                        'TRANSACTION_TYPE' : row[3],
                        'ORIGINATING_MANAGER_ID': row[15],
                        'DESTINATION_MANAGER_ID': row[16],
                        'STATUS' : row[17]
                    },
                    'status_code': 200
                }
                for row in transactions_results
            ]
            return jsonify(formatted_transaction),200
        else:
            return jsonify({'error': 'No Transactions found', 'status_code': 404}), 404
            
    return jsonify({'error': 'Unauthorized access', 'status_code': 404}), 404



def get_image_base64(image_filename):
    try:
        image_path = os.path.join(UPLOAD_FOLDER, image_filename)
        print("Image Path", image_path)
        
        # Check if the image file exists
        if os.path.exists(image_path):
            # Open the image file
            with open(image_path, "rb") as image_file:
                # Read the image and encode it in base64
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                
                # Return the base64 data as an image in base64 format
                return f"data:image/png;base64,{encoded_string}"
            print("Image Location", encoded_string)
        else:
            print(f"Image file {image_filename} not found.")
            return None  # Image not found
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None  # Handle any errors during the process
    