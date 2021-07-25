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
utils.run_query(query, '申立の数が多い会社ランキング')

query = '''
SELECT ppt.company, ppt.state, max(ppt.complaint_count) AS complaint_count
FROM (SELECT company, state, zip_code, count(complaint_id) AS complaint_count
      FROM credit_card_complaints
      WHERE company = 'Citibank'
       AND state IS NOT NULL
      GROUP BY company, state, zip_code
      ORDER BY 4 DESC) ppt
GROUP BY ppt.company, ppt.state
ORDER BY 3 DESC
LIMIT 10;
'''
utils.run_query(query, '↑さっきのクエリに対する加工。外側のGROUP BYにより州ごとで一つになった')

query = '''
SELECT ens.company, ens.state, ens.zip_code, ens.complaint_count
FROM (select company, state, zip_code, count(complaint_id) AS complaint_count
      FROM credit_card_complaints
      WHERE state IS NOT NULL
      GROUP BY company, state, zip_code) ens
INNER JOIN
   (SELECT ppx.company, max(ppx.complaint_count) AS complaint_count
    FROM (SELECT ppt.company, ppt.state, max(ppt.complaint_count) AS complaint_count
          FROM (SELECT company, state, zip_code, count(complaint_id) AS complaint_count
                FROM credit_card_complaints
                WHERE company = 'Citibank'
                 AND state IS NOT NULL
                GROUP BY company, state, zip_code
                ORDER BY 4 DESC) ppt
          GROUP BY ppt.company, ppt.state
          ORDER BY 3 DESC) ppx
    GROUP BY ppx.company) apx
ON apx.company = ens.company
 AND apx.complaint_count = ens.complaint_count
ORDER BY 4 DESC;
'''
utils.run_query(query, '複数のサブクエリ…最終的に最大の申し立て件数を取得する')

query = '''
SELECT ens.company, ens.state, ens.zip_code, ens.complaint_count
FROM (select company, state, zip_code, count(complaint_id) AS complaint_count
      FROM credit_card_complaints
      WHERE state IS NOT NULL
      GROUP BY company, state, zip_code) ens
INNER JOIN
   (SELECT ppx.company, max(ppx.complaint_count) AS complaint_count
    FROM (SELECT ppt.company, ppt.state, max(ppt.complaint_count) AS complaint_count
          FROM (SELECT company, state, zip_code, count(complaint_id) AS complaint_count
                FROM credit_card_complaints
                WHERE company = 'Citibank'
                 AND state IS NOT NULL
                GROUP BY company, state, zip_code
                ORDER BY 4 DESC) ppt
          GROUP BY ppt.company, ppt.state
          ORDER BY 3 DESC) ppx
    GROUP BY ppx.company) apx
ON apx.company = ens.company
 AND apx.complaint_count = ens.complaint_count
ORDER BY 4 DESC;
'''
utils.run_query(query, '↑の件数一覧にしたバージョン…のはずだが中身が変わらない')
