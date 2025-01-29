from app.db import mysql 

class Authentication:
    
    # method signup
    @staticmethod
    def add_user(email, password):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)",
                           (email, password))
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
                 SELECT credentials.credencials_id, credentials.role, credentials.Users_ID, users_of_credit_union.email, users_of_credit_union.credit_union_id, users_of_credit_union.first_name, users_of_credit_union.status FROM credentials INNER JOIN users_of_credit_union ON credentials.users_id = users_of_credit_union.credit_union_user_id WHERE users_of_credit_union.email = %s AND credentials.password = %s ORDER BY credentials.credencials_id DESC
            """, (email, password))
            user = cursor.fetchone()
        return user 

# Deposit Method
class CreditUnion_deposit:
    def push_transaction_desopit(first_name, last_name, transaction_type, amount, account_number, customer_id_number, customer_id_image, credit_union_destination_id, credit_union_originating_id, teller_name_id, date):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO transactions (CUSTOMER_FIRST_NAME, CUSTOMER_LAST_NAME, TRANSACTION_TYPE, AMOUNT, ACCOUNT_NUMBER, CUSTOMER_ID, CUSTOMER_ID_CARD_IMAGE, CREDIT_UNION_DESTINATION_ID, CREDIT_UNION_ORIGINATING_ID, TELLER_NAME, DATE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (first_name, last_name, transaction_type, amount, account_number, customer_id_number, customer_id_image, credit_union_destination_id, credit_union_originating_id, teller_name_id, date))
            mysql.connection.commit()
            cursor.close()
            return {'Customer Name': first_name}
        except Exception as e:
            print(e)
            return None


class CreditUnionmodel:
        def get_credit_unions():
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                                SELECT * FROM `creditunions` WHERE `Status`= 'enabled'
                            """)
                creditunion_result = cursor.fetchall()
            return creditunion_result
        

class all_CreditUnionmodels:
        def get_all_credit_unions():
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                                SELECT * FROM `creditunions`
                            """)
                creditunion_result = cursor.fetchall()
            return creditunion_result
        
            
        def register_the_creditunion(Credit_Union,address,phone_number,email,status):
            try:
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO creditunions (name,address,phone_number,email,Status) VALUES (%s,%s,%s,%s)",
                            (Credit_Union,address,phone_number,email,status))
                
                mysql.connection.commit()
                cursor.close()
                return {'New User': Credit_Union}
            except Exception as e:
                print(e)
                return None
        
class disbursingfunds:
    def get_funds_transaction(transaction_ID):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM transactions WHERE TRANSACTION_ID = %s ; 
                           """, (transaction_ID))
            full_confirmation = cursor.fetchone()
        return full_confirmation


class all_transactions_teller:
    def get_transactions_all_teller(credit_union_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                                SELECT `TRANSACTION_ID`, `CUSTOMER_FIRST_NAME`, `CUSTOMER_LAST_NAME`, 
                                       `TRANSACTION_TYPE`, `AMOUNT`, `CREDIT_UNION_DESTINATION_ID`, `TIMESTAMP`
                                FROM `transactions` 
                                WHERE `CREDIT_UNION_ORIGINATING_ID` = %s ;
            """, (credit_union_id,))
            transaction_result = cursor.fetchall()
        return transaction_result
    
# Transactions on Transation Page on teller account
class all_transactions_on_transations_page_teller:
    def all_transactions_transactions_page_by_teller(credit_union_id,credit_union_id_repeat):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                               SELECT 
                                    t.*,
                                    CONCAT(uo.first_name, ' ', uo.last_name) AS ORIGINATING_MANAGER_ID,
                                    CONCAT(ud.first_name, ' ', ud.last_name) AS DESTINATION_MANAGER_ID,
                                    CASE
                                        WHEN t.ORIGINATING_MANAGER_ID IS NULL AND t.DESTINATION_MANAGER_ID IS NULL THEN 'pending'
                                        WHEN t.ORIGINATING_MANAGER_ID IS NOT NULL AND t.DESTINATION_MANAGER_ID IS NULL THEN 'OM Approved'
                                        WHEN t.ORIGINATING_MANAGER_ID IS NULL AND t.DESTINATION_MANAGER_ID IS NOT NULL THEN 'DM Approved'
                                        WHEN t.ORIGINATING_MANAGER_ID IS NOT NULL AND t.DESTINATION_MANAGER_ID IS NOT NULL THEN 'Approved'
                                    END AS status
                                FROM transactions t
                                LEFT JOIN users_of_credit_union uo 
                                    ON t.ORIGINATING_MANAGER_ID = uo.credit_union_user_id
                                LEFT JOIN users_of_credit_union ud 
                                    ON t.DESTINATION_MANAGER_ID = ud.credit_union_user_id
                                WHERE t.CREDIT_UNION_ORIGINATING_ID = %s OR t.CREDIT_UNION_DESTINATION_ID = %s;
            """, (credit_union_id,credit_union_id_repeat,))
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
    

class users_of_credit_union:
    def get_users_of_credit_union(user_id_session):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                            SELECT * FROM users_of_credit_union WHERE credit_union_user_id = %s ; 
                           """, (user_id_session,))
            get_user = cursor.fetchone()
            
        return get_user

    

class update_transaction:
    def get_update_transaction(user_id_session,transaction_ID):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE transactions SET ORIGINATING_MANAGER_ID = %s WHERE TRANSACTION_ID = %s",
                           (user_id_session,transaction_ID))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': user_id_session} 
        except Exception as e:
            print(e)  
            return None
    
    def get_update_transaction_destination_manager(user_id_session,transaction_ID):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE transactions SET DESTINATION_MANAGER_ID = %s WHERE TRANSACTION_ID = %s",
                           (user_id_session,transaction_ID))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': user_id_session} 
        except Exception as e:
            print(e)  
            return None
       

class add_a_user:
    def add_new_user(first_name, last_name, email, phone_number, credit_union, status):
        try:
            print(first_name, last_name, email, phone_number, credit_union, status)
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users_of_credit_union (first_name, last_name, email, phone_number, credit_union_id, status) VALUES (%s,%s,%s,%s,%s,%s)",
                           (first_name, last_name, email, phone_number, credit_union, status))
            
            mysql.connection.commit()
            cursor.close()
            return {'New User': first_name}
        except Exception as e:
            print(e)
            return None


class new_passwords:
    def get_password(user_id, teller, hashed_password):
        try:
            print(user_id, teller, hashed_password)
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO credentials (Users_ID, password, role) VALUES (%s,%s,%s)",
                           (user_id, hashed_password,teller))
            
            mysql.connection.commit()
            cursor.close()
            return {'New User': user_id}
        except Exception as e:
            print(e)
            return None
        
    def change_password(credentials_id,hashed_password):
        try:
            print(credentials_id,hashed_password)
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE credentials SET password = %s WHERE credencials_id = %s",
                           (hashed_password,credentials_id))
            
            mysql.connection.commit()
            cursor.close()
            return {'New User': credentials_id}
        except Exception as e:
            print(e)
            return None


class all_users:
    def get_all_users(credit_union_id, user_id):
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                           SELECT * FROM users_of_credit_union WHERE credit_union_id = %s  AND credit_union_user_id != %s ; 
                           """, (credit_union_id,user_id,))
            get_users = cursor.fetchall()
        return get_users
    
    def update_user(credit_union_user_id,first_name, last_name, email, phone_number, status):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE users_of_credit_union SET first_name = %s, last_name = %s, email = %s, phone_number = %s, status = %s WHERE credit_union_user_id = %s",
                           (first_name, last_name, email, phone_number, status, credit_union_user_id))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': credit_union_user_id} 
        except Exception as e:
            print(e)  
            return None
    


        

        







