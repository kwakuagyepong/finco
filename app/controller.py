from app.models import Authentication
import hashlib

class AuthenticationController:
    #method for hashing passwords    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    # New method to signup
    @staticmethod
    def add_user(email, password):
        hashed_password = AuthenticationController.hash_password(password)
        return Authentication.add_user(email, hashed_password)
    
    # New method to signin
    @staticmethod
    def get_user(email, password):
        hashed_password = AuthenticationController.hash_password(password)
        return Authentication.get_a_user(email, hashed_password)
    
     