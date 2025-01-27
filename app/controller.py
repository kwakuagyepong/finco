from app.models import Authentication,new_passwords
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
    
        # New method to signin
    @staticmethod
    def get_user_password(user_id, teller, users_password):
        hashed_password = AuthenticationController.hash_password(users_password)
        return new_passwords.get_password(user_id, teller, hashed_password)
    
    @staticmethod
    def change_user_password(credentials_id,users_password):
        hashed_password = AuthenticationController.hash_password(users_password)
        return new_passwords.get_password(credentials_id,hashed_password)
    

    
     