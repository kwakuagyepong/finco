from flask import request, jsonify
from functools import wraps
from app.models import Token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        if not Token.query.filter_by(token=token).first():
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)
    
    return decorated
