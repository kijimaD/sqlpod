import utils_k

print('* ' + 'データ加工100本ノック')

query = '''
select *
from receipt
limit 10
'''
utils_k.run_query(query, 'S-001: レシート明細テーブル（receipt）から全項目を10件抽出し、どのようなデータを保有しているか目視で確認せよ。')
