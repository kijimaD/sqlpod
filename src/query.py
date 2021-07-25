import utils

query = '''
SELECT *
  FROM credit_card_complaints
 LIMIT 100;
'''
utils.run_query(query, '基本形')

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
utils.run_query(query, 'IS NOT NULL')

query = '''
SELECT COUNT(*)
  FROM credit_card_complaints
 WHERE consumer_complaint_narrative IS NULL;
'''
utils.run_query(query, 'IS NULL')
