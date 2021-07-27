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

query = '''
SELECT company AS c
  FROM credit_card_complaints
 GROUP BY c
'''
utils.run_query(query, 'SELECTが先に実行されるので、別名をGROUP BYで使うことはできない。PostgreSQLでは実行可能。')

query = '''
SELECT distinct company
  FROM credit_card_complaints
'''
utils.run_query(query, '↓と同じ')

query = '''
SELECT company
  FROM credit_card_complaints
 GROUP BY company
'''
utils.run_query(query, '↑と同じ')

query = '''
SELECT company, COUNT(*)
  FROM credit_card_complaints
 GROUP BY company
HAVING COUNT(*) = 2;
'''
utils.run_query(query, '集約したグループから含まれる行数が2行のものを選択する。集約に対して条件を指定するのがHAVING')

query = '''
SELECT company, COUNT(*)
  FROM credit_card_complaints
 GROUP BY company
'''
utils.run_query(query, 'HAVINGがないバージョン')

query = '''
SELECT company, AVG(CAST(complaint_id AS INT))
  FROM credit_card_complaints
 GROUP BY company
 HAVING AVG(CAST(complaint_id AS INT)) <= 100000;
'''
utils.run_query(query, 'HAVINGで条件指定する')

query = '''
SELECT company, AVG(CAST(complaint_id AS INT))
  FROM credit_card_complaints
 GROUP BY company
'''
utils.run_query(query, 'HAVINGがないバージョン')

query = '''
SELECT company, issue
  FROM credit_card_complaints
 ORDER BY company, issue
'''
utils.run_query(query, 'ORDER BY 複数')

query = '''
SELECT company AS c
  FROM credit_card_complaints
 ORDER BY c
'''
utils.run_query(query, 'ソートキーに別名が使用できる')
