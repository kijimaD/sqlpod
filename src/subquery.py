import utils

print('* ' + 'サブクエリ')

query = '''
SELECT ccd.complaint_id, ccd.product, ccd.company, ccd.zip_code
FROM (SELECT complaint_id, product, company, zip_code
      FROM credit_card_complaints
      WHERE zip_code = '91701') ccd LIMIT 10;
'''
utils.run_query(query, 'サブクエリ')

query = '''
SELECT complaint_id, product, company, zip_code
      FROM credit_card_complaints
      where zip_code = '91701'
'''
utils.run_query(query, 'サブクエリの中の方')

query = '''
SELECT company, state, zip_code, count(complaint_id) AS complaint_count
FROM credit_card_complaints
WHERE company = 'Citibank' AND state IS NOT NULL
GROUP BY company, state, zip_code
ORDER BY 4 DESC
LIMIT 10;
'''
