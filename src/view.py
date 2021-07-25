import utils

print('* ' + 'ビュー')

command = '''
CREATE VIEW credit_card_w_complaints AS
    SELECT * FROM credit_card_complaints
    WHERE consumer_complaint_narrative IS NOT NULL;
'''
utils.run_command(command, 'credit_wを作成する')

command = '''
CREATE VIEW credit_card_wo_complaints as
    SELECT * FROM credit_card_complaints
    WHERE consumer_complaint_narrative IS NULL;
'''
utils.run_command(command, 'credit_woを作成する')

command = '''
CREATE VIEW bank_account_w_complaints AS
    SELECT * FROM bank_account_complaints
    WHERE consumer_complaint_narrative IS NOT NULL;
'''
utils.run_command(command, 'bank_wを作成する')

command = '''
CREATE VIEW bank_account_wo_complaints AS
    SELECT * FROM bank_account_complaints
    WHERE consumer_complaint_narrative IS NULL;
'''
utils.run_command(command, 'bank_woを作成する')

query = '''
SELECT * FROM credit_card_w_complaints LIMIT 5;
'''
utils.run_query(query, 'viewから取得する')

command = '''
CREATE VIEW with_complaints AS
    SELECT * FROM credit_card_w_complaints
    UNION ALL
    SELECT * FROM bank_account_w_complaints;
'''
utils.run_command(command, 'UNION')

query = '''
SELECT * FROM with_complaints LIMIT 5;
'''
utils.run_query(query, 'with_complaints表示')

command = '''
CREATE VIEW without_complaints AS
    SELECT * FROM credit_card_wo_complaints
    UNION ALL
    SELECT * FROM bank_account_wo_complaints;
'''
utils.run_command(command, 'UNION')

query = '''
SELECT * FROM without_complaints LIMIT 5;
'''
utils.run_query(query, 'without_complaints表示')

query = '''
SELECT count(*) FROM credit_card_wo_complaints;
'''
utils.run_query(query, 'credit_card_without_complaints')

query ='''
SELECT count(*)
FROM without_complaints
'''
utils.run_query(query, '申し立てがない')

query ='''
SELECT count(*)
FROM
  (SELECT *
   FROM without_complaints
   EXCEPT SELECT *
   FROM credit_card_wo_complaints) ppg;
'''
utils.run_query(query, 'クレジットカードの申立がないものを除外')

query = '''
SELECT complaint_id, product, company, zip_code,
       complaint_id || '-' || product || '-' || company || '-' ||
 zip_code AS concat
FROM credit_card_complaints
LIMIT 10
'''
utils.run_query(query, '合成したカラムを表示する')
