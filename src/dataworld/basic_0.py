import utils

print('* ' + '基本的操作')

"""
query = '''

'''
utils.run_query(query, '')
"""

query = '''
SELECT issue AS mondai
  FROM credit_card_complaints
 LIMIT 100;
'''
utils.run_query(query, 'ASでカラムに別名をつける。dataworldではダブルクオートをつけても日本語を使えないよう')

query = '''
SELECT DISTINCT company
  FROM credit_card_complaints;
'''
utils.run_query(query, 'DISTINCTを使ってcompanyの重複をなくす')

query = '''
SELECT DISTINCT company, state
  FROM credit_card_complaints;
'''
utils.run_query(query, 'DISTINCTしたレコードのほかのカラムを出す')

query = '''
SELECT issue
  FROM credit_card_complaints
 WHERE company = 'Citibank'
 LIMIT 100;
'''
utils.run_query(query, 'WHEREで条件指定する')

query = '''
SELECT complaint_id, (CAST(complaint_id as float) * 2) as complaint_id_x2
  FROM credit_card_complaints
 LIMIT 100;
'''
utils.run_query(query, '値を2倍にしたカラムを作成')

query = '''
SELECT 100 * 3 as keisan;
'''
utils.run_query(query, '計算機として使う...FROMは不要')

query = '''
SELECT *
  FROM credit_card_complaints
 WHERE product <> 'Credit card'
 LIMIT 100;
'''
utils.run_query(query, '否定演算子 - 結果はNo results')

query = '''
SELECT complaint_id
  FROM credit_card_complaints
 WHERE CAST(complaint_id AS float) >= 460000
 LIMIT 100;
'''
utils.run_query(query, '数値で条件指定')

query = '''
SELECT complaint_id
  FROM credit_card_complaints
 WHERE CAST(complaint_id AS FLOAT) + CAST(zip_code AS FLOAT) >= 460000
 LIMIT 100;
'''
utils.run_query(query, '計算結果で条件指定')

query = '''
SELECT company, tags
  FROM credit_card_complaints
 WHERE tags IS NULL
 LIMIT 100;
'''
utils.run_query(query, 'NULLに比較演算子は使えない。IS NULLを使う')

query = '''
SELECT *
  FROM
(SELECT company, tags
   FROM credit_card_complaints
  WHERE tags IS NULL
  LIMIT 100) null_tag
 WHERE tags <> '280';
'''
utils.run_query(query, '↑の結果のnullに対して<>を使っても認識しないことを確認')

query = '''
SELECT company, tags
  FROM credit_card_complaints
 WHERE tags IS NOT NULL
 LIMIT 100;
'''
utils.run_query(query, 'NULLでないときはIS NOT NULLを使う')

query = '''
SELECT product, complaint_id
  FROM credit_card_complaints
 WHERE NOT CAST(complaint_id AS FLOAT) >= 400000
 LIMIT 100
'''
utils.run_query(query, 'NOTで条件反転')

query = '''
SELECT company, issue
  FROM credit_card_complaints
 WHERE company = 'Citibank'
   AND issue = 'Late fee'
    OR issue = 'Payoff process'
 LIMIT 100
'''
utils.run_query(query, 'ORでおかしくなる例。companyの条件が無視されている。ANDが優先されるためカッコが必要。')

query = '''
SELECT company, issue
  FROM credit_card_complaints
 WHERE company = 'Citibank'
    AND (issue = 'Late fee'
        OR issue = 'Payoff process')
 LIMIT 100
'''
utils.run_query(query, 'カッコをつけて正しい結果になった')

query = '''
SELECT complaint_id,
       (CAST(complaint_id AS float) * 2) AS complaint_id_x2
FROM credit_card_complaints
where (CAST(complaint_id AS float) * 2) > 1000000
LIMIT 100;
'''
utils.run_query(query, '計算した値を条件に使う')
