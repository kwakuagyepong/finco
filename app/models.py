from app.db import mysql 
from flask import session

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
    def push_transaction_desopit(first_name, last_name, transaction_type, amount, account_number, customer_id_number, customer_id_image, credit_union_destination_id, credit_union_originating_id, teller_name_id, date,originating_manager_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO transactions (CUSTOMER_FIRST_NAME, CUSTOMER_LAST_NAME, TRANSACTION_TYPE, AMOUNT, ACCOUNT_NUMBER, CUSTOMER_ID, CUSTOMER_ID_CARD_IMAGE, CREDIT_UNION_DESTINATION_ID, CREDIT_UNION_ORIGINATING_ID, TELLER_NAME, DATE, ORIGINATING_MANAGER_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (first_name, last_name, transaction_type, amount, account_number, customer_id_number, customer_id_image, credit_union_destination_id, credit_union_originating_id, teller_name_id, date,originating_manager_id))
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
        
            
        def register_the_creditunion(Credit_Union,address,address_2,phone_number,email,status):
            try:
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO creditunions (name,address,address_2,phone_number,email,Status) VALUES (%s,%s,%s,%s,%s,%s)",
                            (Credit_Union,address,address_2,phone_number,email,status))
                
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
                           """, (transaction_ID,))
            full_confirmation = cursor.fetchone()
        return full_confirmation
    
    def update_transaction_status(transaction_ID, status):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE transactions SET status_transaction = %s WHERE TRANSACTION_ID = %s",
                           (status, transaction_ID))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': transaction_ID}
        except Exception as e:
            print(e)
            return None
    

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
    
# Get Transactions of specific credit unions where status is not disbursed
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
                                    END AS STATUS
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
            # print(first_name, last_name, email, phone_number, credit_union, status)
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users_of_credit_union (first_name, last_name, email, phone_number, credit_union_id, status) VALUES (%s,%s,%s,%s,%s,%s)",
                           (first_name, last_name, email, phone_number, credit_union, status))
            
            mysql.connection.commit()
            cursor.close()
            return {'New User': first_name}
        except Exception as e:
            print(e)
            return None

# Assign Passwords
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

    def change_password(the_credentials,hashed_password):
        try:
            print("After encyption: ", the_credentials,hashed_password)
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE credentials SET password = %s WHERE credencials_id = %s",
                           (hashed_password,the_credentials))
            mysql.connection.commit()
            cursor.close()
            return {'New User': the_credentials}
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
        
class user_status:
    def get_status(user_id,user_status_current):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE users_of_credit_union SET status = %s WHERE credit_union_user_id = %s",
                           (user_status_current, user_id))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': user_id}
        except Exception as e:
            print(e)
            return None
    


# Below are functions for amking checks eg.
class checks:
    def check_for_data_for_credentials_tables(user_id):
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM credentials WHERE Users_ID = %s
                            """, (user_id,))
                get_credentials_data = cursor.fetchone()
            
            # Return the fetched data (could be None if no data is found)
            return get_credentials_data
        
        except mysql.connector.Error as err:
            # Handle any database errors
            print(f"Database error: {err}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None



class accounts:
    # Get data on Credit Union Accounts with Inner join credit union name
    def get_credit_union_accounts():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT accounts.*, creditunions.name AS credit_union_name
                            FROM accounts
                            INNER JOIN creditunions
                            ON accounts.credit_union_id = creditunions.credit_union_id;
                            """,)
                get_credit_union_accounts_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_credit_union_accounts_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        # ------------------------- For disbursing funds Start-------------------------
    def get_account_data_for_disburse_destination_creditunion(CREDIT_UNION_DESTINATION_ID):
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM accounts WHERE credit_union_id = %s;
                            """,(CREDIT_UNION_DESTINATION_ID,))
                account_data = cursor.fetchone()
            # Return the fetched data (could be None if no data is found)
            return account_data

        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        
    def get_account_data_for_disburse_originating_creditunion(CREDIT_UNION_ORIGINATING_ID):
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM accounts WHERE credit_union_id = %s;
                            """,(CREDIT_UNION_ORIGINATING_ID,))
                account_data = cursor.fetchone()
            # Return the fetched data (could be None if no data is found)
            return account_data

        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
    
    def update_account_amount_for_orginating_and_destination(CREDIT_UNION_ORIGINATING_ID,account_amount_update_for_originating_crediunion,CREDIT_UNION_DESTINATION_ID ,account_amount_update_for_destination_crediunion):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE accounts SET amount = CASE WHEN credit_union_id = %s THEN %s WHEN credit_union_id = %s THEN %s ELSE amount END WHERE credit_union_id IN (%s, %s);",
                           (CREDIT_UNION_ORIGINATING_ID, account_amount_update_for_originating_crediunion, CREDIT_UNION_DESTINATION_ID, account_amount_update_for_destination_crediunion, CREDIT_UNION_ORIGINATING_ID, CREDIT_UNION_DESTINATION_ID))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': [CREDIT_UNION_ORIGINATING_ID, CREDIT_UNION_DESTINATION_ID]}
        except Exception as e:
            print(e)
            return None
        # ------------------------- For disbursing funds End --------------------------------

# Get data for Account Deposit History (This is for Admin Access)
    def get_accounts_deposite_history():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM account_deposit_history
                            """,)
                get_accounts_deposite_history_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_accounts_deposite_history_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        
    def get_accounts_deposite_history_by_credit_union(credit_union_id):
        print(credit_union_id)
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM account_deposit_history WHERE credit_union_id = %s
                            """,(credit_union_id,))
                accounts_deposite_history_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return accounts_deposite_history_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None

# Get data for Account Deposit History (This is for Admin Access)
    def get_accounts_deposite_history():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM account_deposit_history
                            """,)
                get_accounts_deposite_history_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_accounts_deposite_history_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        
# Insert into Account Deposit History
    def insert_into_account_deposit_history(amount,credit_union_id,user_id):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO account_deposit_history (credit_union_id,amount,user_id) VALUES (%s,%s,%s)",
                           (credit_union_id,amount,user_id))
            mysql.connection.commit()
            cursor.close()
            return {'Credit Union': credit_union_id}
        except Exception as e:
            print(e)
            return None

class Admin_use:
    def all_users_full_data():
        assigned_role = session['role']

        if assigned_role == 'admin':
            try:
                # Assuming mysql.connection is already established and available
                with mysql.connection.cursor() as cursor:
                    cursor.execute("""
                                SELECT 
                                        credentials.role, 
                                        credentials.Users_ID, 
                                        users_of_credit_union.First_name, 
                                        users_of_credit_union.Last_name, 
                                        users_of_credit_union.email, 
                                        users_of_credit_union.phone_number, 
                                        users_of_credit_union.status, 
                                        creditunions.name
                                    FROM credentials
                                    INNER JOIN users_of_credit_union ON credentials.Users_ID = users_of_credit_union.credit_union_user_id
                                    INNER JOIN creditunions ON users_of_credit_union.credit_union_id= creditunions.credit_union_id;
                                """,)
                    get_credentials_data = cursor.fetchall()
                # Return the fetched data (could be None if no data is found)
                return get_credentials_data
        
            except Exception as e:
                # Handle any other exceptions
                print(f"An error occurred: {e}")
                return None
               
    def all_transactions():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM transactions
                            """,)
                get_credentials_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_credentials_data
        
        except mysql.connector.Error as err:
            # Handle any database errors
            # print(f"Database error: {err}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        
    def set_manager(credit_Union,users_id,role):
        try:
            cursor = mysql.connection.cursor()
            # Insert into managers table
            cursor.execute("""
                       INSERT INTO managers (users_id,credit_union_id) VALUES (%s, %s)
                        """, (users_id,credit_Union))
            
             # Update role in credentials table
            cursor.execute("UPDATE credentials SET role = %s WHERE Users_ID = %s",
                           (role,users_id))
            mysql.connection.commit()
            cursor.close()
            return {'Updated': users_id} 
        except Exception as e:
            print(e)  
            return None

    def all_credit_union_managers():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM managers
                            """,)
                get_credentials_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_credentials_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        

    def view_manager_information():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT 
                                    managers.id AS manager_id,
                                    users_of_credit_union.first_name,
                                    users_of_credit_union.last_name,
                                    users_of_credit_union.status,
                                    creditunions.name AS credit_union_name,
                                    creditunions.address,
                                    creditunions.address_2,
                                    creditunions.credit_union_id, 
                                    creditunions.phone_number,
                                    creditunions.Status,
                                    creditunions.email
                                FROM managers
                                INNER JOIN users_of_credit_union ON managers.users_id = users_of_credit_union.credit_union_user_id
                                INNER JOIN creditunions ON managers.credit_union_id = creditunions.credit_union_id; 
                            """,)
                get_credentials_data = cursor.fetchall()
            # Return the fetched data (could be None if no data is found)
            return get_credentials_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        

    def check_existing_user(users_id):
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM managers WHERE users_id = %s
                            """,(users_id,))
                get_credentials_data = cursor.fetchone()
            # Return the fetched data (could be None if no data is found)
            return get_credentials_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
    
    def get_transaction_charge():
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM transaction_charges
                            """,)
                get_transaction_charge_data = cursor.fetchone()
            # Return the fetched data (could be None if no data is found)
            return get_transaction_charge_data
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
        
    def updated_credit_union_status(Credit_Union_id,status):
            try:
                cursor = mysql.connection.cursor()
                cursor.execute("UPDATE creditunions SET Status = %s WHERE credit_union_id = %s",
                               (status, Credit_Union_id))
                mysql.connection.commit()
                cursor.close()
                return {'Updated': Credit_Union_id}
            except Exception as e:
                print(e)    
                return None
            
    def update_credit_union_data(Credit_Union_id,Credit_Union,address,address_2,phone_number,email):
            try:
                cursor = mysql.connection.cursor()
                cursor.execute("UPDATE creditunions SET name = %s, address = %s,address_2 = %s, phone_number = %s, email = %s WHERE credit_union_id = %s",
                               (Credit_Union,address,address_2,phone_number,email,Credit_Union_id))
                mysql.connection.commit()
                cursor.close()
                return {'Updated': Credit_Union_id}
            except Exception as e:
                print(e)    
                return None
            
    def get_cap_amount(CREDIT_UNION_ORIGINATING_ID):
        try:
            # Assuming mysql.connection is already established and available
            with mysql.connection.cursor() as cursor:
                cursor.execute("""
                            SELECT * FROM amount_cup WHERE credit_union_id = %s
                            """,(CREDIT_UNION_ORIGINATING_ID,))
                get_amount_cup = cursor.fetchone()
            # Return the fetched data (could be None if no data is found)
            return get_amount_cup
        
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None
            
        





