from app.db import mysql 

class Authentication:
    
    # method signup
    @staticmethod
    def add_user(email, password):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)",
                           (email, password,))
            mysql.connection.commit()
            cursor.close()
            return {'email': email, 'password': password} 
        except Exception as e:
            print(e)  
            return None
      
    # method signin
    @staticmethod
    def get_a_user(email, password):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                 SELECT credentials.credencials_id, credentials.role, users_of_credit_union.email, users_of_credit_union.credit_union_id, users_of_credit_union.first_name, users_of_credit_union.status FROM credentials INNER JOIN users_of_credit_union ON credentials.users_id = users_of_credit_union.credit_union_user_id WHERE users_of_credit_union.email = %s AND credentials.password = %s ORDER BY credentials.credencials_id DESC
            """, (email, password))
            user = cursor.fetchone()
        return user 


class CreditUnionmodel:
        def get_credit_unions():
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                                SELECT * from creditunions WHERE Status = 'Enabled'
                            """)
                creditunion_result = cursor.fetchall()
            
            return creditunion_result
        
class all_transactions:
    def get_transactions_all(creditunion_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                                SELECT * FROM `transactions` WHERE 
                           `CREDIT_UNION_DESTINATION_ID` = %s OR `CREDIT_UNION_ORIGINATING_ID` = %s ;
            """, (creditunion_id, creditunion_id))
            transaction_result = cursor.fetchall()

        return transaction_result
        
        

class all_transaction_inbound:
    def get_inbound_transactions_all(creditunion_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                                SELECT * FROM `transactions` WHERE `CREDIT_UNION_ID_INBOUND` = %s ;
            """, (creditunion_id))
            transaction_result = cursor.fetchall()

        return transaction_result    



