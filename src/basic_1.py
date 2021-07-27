import utils

print('* ' + '集計関数')

query = '''
SELECT count(*), count(tags)
  FROM credit_card_complaints
'''
utils.run_query(query, 'COUNTで数を数える/nullのtagsカラムを除外してカウントする')

query = '''
SELECT SUM(cast(complaint_id AS int))
  FROM credit_card_complaints
'''
utils.run_query(query, '苦情IDを合算する')

query = '''
SELECT AVG(cast(complaint_id AS int))
  FROM credit_card_complaints
'''
utils.run_query(query, '苦情IDの平均')

query = '''
SELECT MAX(cast(complaint_id AS int)), MIN(cast(complaint_id AS int))
  FROM credit_card_complaints
'''
utils.run_query(query, '最小・最大の苦情ID')

query = '''
SELECT COUNT(DISTINCT company)
  FROM credit_card_complaints
'''
utils.run_query(query, '重複なしの会社の数。COUNTとDISTINCTを使う')

query = '''
SELECT issue, COUNT(issue)
  FROM credit_card_complaints
 GROUP BY issue
 ORDER BY count DESC
'''
utils.run_query(query, '苦情の理由ランキング')

query = '''
SELECT issue, COUNT(issue)
  FROM credit_card_complaints
 WHERE company = 'Citibank'
 GROUP BY issue
 ORDER BY count DESC
'''
utils.run_query(query, 'Citibankの苦情の理由ランキング。条件の位置に注意')
