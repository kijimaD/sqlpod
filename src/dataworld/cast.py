import utils

print('* ' + 'キャスト')

query = '''
SELECT CAST(complaint_id AS float) AS complaint_id
FROM bank_account_complaints LIMIT 10;
'''
utils.run_query(query, 'floatに型キャストする')

query = '''
SELECT CAST(complaint_id AS int) AS complaint_id,
       date_received, product, sub_product, issue, company,
       state, zip_code, submitted_via, date_sent, company_response_to_consumer,
       timely_response, consumer_disputed
FROM bank_account_complaints
WHERE state = 'CA'
    AND consumer_disputed = 'No'
    AND company = 'Wells Fargo & Company'
LIMIT 5;
'''
utils.run_query(query, 'intに型キャストする')
