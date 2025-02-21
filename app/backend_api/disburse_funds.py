from flask import Blueprint, jsonify, request, session
from app.models import disbursingfunds, accounts

def get_funds_data():
    
    required_fields = ['transaction_ID'] 
    data = request.json
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        error_message = f"Missing fields: {', '.join(missing_fields)}"
        return jsonify({'error': error_message, 'status_code': 400}), 400
    
    transaction_ID = data['transaction_ID']
    full_data = disbursingfunds.get_funds_transaction(transaction_ID)
    print(full_data)
    if full_data:
        TRANSACTION_TYPE = [3]
        CREDIT_UNION_DESTINATION_ID = [8]
        CREDIT_UNION_ORIGINATING_ID = [9]
        ORIGINATING_MANAGER_ID = [11]
        DESTINATION_MANAGER_ID = [12]
        AMOUNT = [4]

        if not ORIGINATING_MANAGER_ID or not DESTINATION_MANAGER_ID or not AMOUNT:
            return jsonify({
                'error': 'error releasing funds. Transaction has not been approved',
                'status_code': 400
            }), 400
        else:
            get_creditunion_destination_account_data = accounts.get_account_data_for_disburse_destination_creditunion(CREDIT_UNION_DESTINATION_ID)
            if get_creditunion_destination_account_data:
                CREDIT_UNION_DESTINATION_ID_AMOUNT = [1]
            else: 
                return jsonify({
                    'error': 'error show destination account data. Destination account not found',
                    'status_code': 400
                }), 400

            get_creditunion_destination_account_data = accounts.get_account_data_for_disburse_destination_creditunion(CREDIT_UNION_ORIGINATING_ID)
            if get_creditunion_destination_account_data:
                CREDIT_UNION_ORIGINATING_ID_AMOUNT = [1]
            else: 
                return jsonify({
                    'error': 'error show originating account data. Originating account not found',
                    'status_code': 400
                }), 400
            

            if TRANSACTION_TYPE == 'CREDIT':
              account_amount_update_for_originating_crediunion = CREDIT_UNION_ORIGINATING_ID_AMOUNT - AMOUNT
              account_amount_update_for_destination_crediunion = CREDIT_UNION_DESTINATION_ID_AMOUNT + AMOUNT
            elif TRANSACTION_TYPE == 'DEBIT':
                account_amount_update_for_originating_crediunion = CREDIT_UNION_ORIGINATING_ID_AMOUNT + AMOUNT
                account_amount_update_for_destination_crediunion = CREDIT_UNION_DESTINATION_ID_AMOUNT - AMOUNT
            else:
                return jsonify({
                    'error': 'error updating account. Transaction type not found',
                    'status_code': 400
                }), 400
            transaction_status = 'disbursed'
            
            result_after_update_of_amount = accounts.update_account_amount_for_orginating_and_destination(CREDIT_UNION_ORIGINATING_ID,account_amount_update_for_originating_crediunion,CREDIT_UNION_DESTINATION_ID ,account_amount_update_for_destination_crediunion)
            if result_after_update_of_amount:
                return jsonify({
                    'data': 'Amount has been disbursed successfully',
                    'status_code': 200
                }), 200
                
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
            

            

            
            
            




                    
                    

                






            # if each transaction is charged:
            # get_transaction_charge = Admin_use.get_transaction_charge()
            # if get_transaction_charge:
            #     charge_data = [0]
            #     charges = charge_data / 100 
            #     result_charge = AMOUNT * charges
            #     customer_amount = AMOUNT - result_charge
                

    return jsonify({'error': 'Transaction not found.', 'status_code': 404}), 404
