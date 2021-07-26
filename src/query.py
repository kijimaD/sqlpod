import utils

print('* ' + '使い方')

query = '''
SELECT *
FROM credit_card_complaints
LIMIT 100;
'''
utils.run_query(query, '全表示')

query = '''
SELECT COUNT(*)
FROM credit_card_complaints;
'''
utils.run_query(query, 'COUNT')

query = '''
SELECT COUNT(*)
FROM credit_card_complaints
WHERE consumer_complaint_narrative IS NOT NULL;
'''
utils.run_query(query, 'where: IS NOT NULL')

query = '''
SELECT COUNT(*)
FROM credit_card_complaints
WHERE consumer_complaint_narrative IS NULL;
'''
utils.run_query(query, 'where: IS NULL')
