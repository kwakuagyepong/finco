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
                                SELECT `credit_union_id`, `name`, `address`, `phone_number`, `email` FROM creditunions WHERE Status = 'Enabled'
                            """)
                creditunion_result = cursor.fetchall()
            return creditunion_result


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



