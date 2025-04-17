from flask import Blueprint, jsonify, request, session
from app.models import disbursingfunds, accounts, Admin_use
from decimal import Decimal

def get_disburse_funds():
    assigned_role = session['role']
    credit_union_id = session['credit_union_id']

    if assigned_role == "teller":
        required_fields = ['TRANSACTION_ID'] 
        data = request.json
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            error_message = f"Missing fields: {', '.join(missing_fields)}"
            return jsonify({'error': error_message, 'status_code': 400}), 400
        
        transaction_ID = data['TRANSACTION_ID']
        full_data = disbursingfunds.get_funds_transaction(transaction_ID)
        # print("Transaction full data", full_data)
        if full_data:
            TRANSACTION_TYPE = full_data[3]
            AMOUNT = full_data[4]
            CREDIT_UNION_DESTINATION_ID = full_data[8]
            CREDIT_UNION_ORIGINATING_ID = full_data[9]
            ORIGINATING_MANAGER_ID = full_data[11]
            DESTINATION_MANAGER_ID = full_data[12]
            status_of_transaction = full_data[15]
            
            if status_of_transaction == 'disbursed':
                return jsonify({
                    'error': 'Error releasing funds. Transaction has already been disbursed',
                    'status_code': 400
                }), 400
            
            # Get the cap amount for the originating credit union
            check_amount_cap = Admin_use.get_cap_amount(CREDIT_UNION_ORIGINATING_ID)
            capped_amount = check_amount_cap[1]
            print("CUP Amount", capped_amount)

            if AMOUNT <= capped_amount:
                # If the transaction is below the cap amount, bypass the originating manager approval
                ORIGINATING_MANAGER_ID = None # Skip the approval check
            else:
                if not ORIGINATING_MANAGER_ID:
                    return jsonify({
                        'error': 'error releasing funds. Transaction has not been approved by the originating manager',
                        'status_code': 400
                    }), 400  

            if not DESTINATION_MANAGER_ID or not AMOUNT:
                full_data = disbursingfunds.get_funds_transaction(transaction_ID)
                return jsonify({
                    'error': 'error releasing funds. Transaction has not been approved',
                    'status_code': 400
                }), 400
            else:
                # Get account balance for the destination creditunion
                get_creditunion_destination_account_data = accounts.get_account_data_for_disburse_destination_creditunion(CREDIT_UNION_DESTINATION_ID)
                # print(get_creditunion_destination_account_data)
                if get_creditunion_destination_account_data:
                    CREDIT_UNION_DESTINATION_ID_AMOUNT = get_creditunion_destination_account_data[1]
                    # print("Credit union destination",CREDIT_UNION_DESTINATION_ID_AMOUNT)
                else: 
                    return jsonify({
                        'error': 'error show destination account data. Destination account not found',
                        'status_code': 400
                    }), 400
                # Get account balance for the ORIGINATING creditunion
                get_creditunion_destination_account_data = accounts.get_account_data_for_disburse_destination_creditunion(CREDIT_UNION_ORIGINATING_ID)
                if get_creditunion_destination_account_data:
                    CREDIT_UNION_ORIGINATING_ID_AMOUNT = get_creditunion_destination_account_data[1]
                    # print("Credit union originating",CREDIT_UNION_ORIGINATING_ID_AMOUNT)
                else: 
                    return jsonify({
                        'error': 'error show originating account data. Originating account not found',
                        'status_code': 400
                    }), 400
                
                coverted_amount = Decimal(AMOUNT)
                # print("Amount converted", coverted_amount)
                if TRANSACTION_TYPE == 'CREDIT':
                    account_amount_update_for_originating_crediunion = CREDIT_UNION_ORIGINATING_ID_AMOUNT - coverted_amount
                    account_amount_update_for_destination_crediunion = CREDIT_UNION_DESTINATION_ID_AMOUNT + coverted_amount
                    # print("new Amount ", account_amount_update_for_originating_crediunion)
                    # print("new Amount ", account_amount_update_for_destination_crediunion)
                elif TRANSACTION_TYPE == 'DEBIT':
                    account_amount_update_for_originating_crediunion = CREDIT_UNION_ORIGINATING_ID_AMOUNT + coverted_amount
                    account_amount_update_for_destination_crediunion = CREDIT_UNION_DESTINATION_ID_AMOUNT - coverted_amount
                    # print("new Amount ", account_amount_update_for_originating_crediunion)
                    # print("new Amount ", account_amount_update_for_destination_crediunion)
                else:
                    return jsonify({
                        'error': 'error updating account. Transaction type not found',
                        'status_code': 400
                    }), 400
                transaction_status = 'disbursed'
                result_after_update_of_amount = accounts.update_account_amount_for_orginating_and_destination(CREDIT_UNION_ORIGINATING_ID,account_amount_update_for_originating_crediunion,CREDIT_UNION_DESTINATION_ID ,account_amount_update_for_destination_crediunion)
                if not result_after_update_of_amount:
                    return jsonify({
                        'Error': 'Error updating account amount. Amount not disbursed',
                        'status_code': 400
                    }), 400
                    
                done = disbursingfunds.update_transaction_status(transaction_ID, transaction_status)
                if done:
                    return jsonify({
                        'data': 'Amount has been disbursed successfully',
                        'status_code': 200
                    }), 200   
                else:
                    return jsonify({
                        'error': 'error updating account transaction. Amount not disbursed',
                        'status_code': 400
                    }), 400
        return jsonify({'error': 'Transaction not found.', 'status_code': 404}), 404

    return jsonify({'error': 'Unauthorized user', 'status_code': 400}), 400
    
