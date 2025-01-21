from flask import Blueprint, jsonify, request, session


def signout():
    # Remove the user from session
    session.pop('credit_union_id', None)  # Remove the credit_union_id
    session.pop('user_id', None)  # Remove the user_id
    return jsonify({'Message': 'User not found', 'status_code': 200}), 200