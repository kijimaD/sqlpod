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
