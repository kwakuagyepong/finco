from flask import jsonify, request, session
from app.models import Admin_use
import os
from io import BytesIO
from PIL import Image
from datetime import datetime
import base64
UPLOAD_FOLDER = 'customer_id_cards'


# All users for Admin
def get_users():
    role = ["admin"]
    assigned_role = session['role']

    if assigned_role in role:
        result_of_users = Admin_use.all_users()
        if result_of_users:
            formatted = [
                {
                    'results': {
                        'id': row[0], 
                        'First Name': row[1],
                        'Last Name ': row[2], 
                        'email': row[3], 
                        'phone number': row[4],
                        'credit Union' : row[5],
                        'status' : row[6]
                    },
                    'status_code': 200
                }
                for row in result_of_users
            ]
            return jsonify(formatted),200
        else:
            return jsonify({'error': 'Users not found', 'status_code': 404}), 404
    return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400

# All transactions for Admin
def get_credit_union_transactions():
    role = ["admin"]
    assigned_role = session['role']

    if assigned_role in role:
        result_of_transactions = Admin_use.all_transactions()
        if result_of_transactions: 
            formatted = [
                {
                    'results': {
                        'TRANSACTION_ID': row[0],
                        'CUSTOMER_FIRST_NAME' : row[1],
                        'CUSTOMER_LAST_NAME' : row[2],
                        'TRANSACTION_TYPE' : row[3],
                        'AMOUNT' : row[4],
                        'ACCOUNT_NUMBER' : row[5],
                        'CUSTOMER_ID' : row[6],
                        'CUSTOMER_ID_CARD_IMAGE' : get_image_base64(row[7]),
                        'CREDIT_UNION_DESTINATION_ID': row[8],
                        'CREDIT_UNION_ORIGINATING_ID': row[9],
                        'TELLER':row[10],
                        'ORIGINATING_MANAGER_ID': row[11],
                        'DESTINATION_MANAGER_ID': row[12],
                        'TIMESTAMP': row[13],
                        # 'TIMESTAMP': row[14],
                        'STATUS' : row[15]
                    },
                    'status_code': 200
                }
                for row in result_of_transactions
            ]
            return jsonify(formatted),200
        else:
            return jsonify({'error': 'Users not found', 'status_code': 404}), 404
    return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400


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






 
