from flask import Flask, jsonify, request
from datetime import datetime
from app.db import mysql


def check_token():
    auth_header = request.headers.get('Authorization')

    # if not auth_header:
    #     return jsonify({'error': 'Unauthorized Request', 'status_code': 401}), 401

    # # Extract the token from the Bearer token string
    # parts = auth_header.split()
    # if len(parts) != 2 or parts[0].lower() != 'bearer':
    #     print("Invalid Authorization header format.")
    #     return jsonify({'error': 'Invalid Authorization Header', 'status_code': 401}), 401

    # token = parts[1]
    token =  "qiwii233j2i3joijoiewoiejoio2i3"

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tokens WHERE token = %s", (token,))
    token_data = cursor.fetchone()

    if not token_data:
        cursor.close()
        print("Token not found in database.")
        return jsonify({'error': 'Invalid Authentication Token', 'status_code': 401}), 401

    # Check token expiration
    expiration_date = token_data[2]  # Assuming expiration_date is the third column
    current_time = datetime.now()
    if expiration_date < current_time:
        cursor.close()
        print("Token has expired.")
        return jsonify({'error': 'Authentication Token Expired', 'status_code': 401}), 401

    cursor.close()
    return None


def register_middleware(app):
    @app.before_request
    def before_request():
        result = check_token()
        if result:
            return result  # Return error response if authorization fails
