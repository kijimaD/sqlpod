import utils

print('* ' + '練習問題')

query = '''
select company, count(company) as company_amt
from credit_card_complaints
group by company
order by company_amt desc
'''
utils.run_query(query, '会社数でカウント')

query = '''
select company, count(company) as company_amt,
    (select count(*) from credit_card_complaints) as total
from credit_card_complaints
group by company
order by company_amt desc
'''
utils.run_query(query, '↑に全レコードカウントカラムを追加した')

query = '''
SELECT *
  FROM (SELECT company, COUNT(company) AS company_amt,
               (SELECT COUNT(*)
                  FROM credit_card_complaints) AS total
          FROM credit_card_complaints
         GROUP BY company
         ORDER BY company_amt DESC) ppg
'''
utils.run_query(query, '↑をfromをネストした(結果は同じ)')

query = '''
SELECT ppg.company, ppg.company_amt, ppg.total,
       ((CAST(ppg.company_amt AS float) / CAST(ppg.total AS float)) * 100) AS percent
  FROM (SELECT company, COUNT(company) AS company_amt, (SELECT COUNT(*)
                                                          FROM credit_card_complaints) AS total
          FROM credit_card_complaints
         GROUP BY company
         ORDER BY company_amt DESC) ppg;
'''
utils.run_query(query, '↑で作成したカラム同士の計算を行う(このクエリはdataworldではキャストがエラーになる)')
