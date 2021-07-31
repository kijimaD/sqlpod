import utils_k as utils

print('* ' + '基本的なクエリの練習')

query = '''
select *
from receipt
limit 10
'''
utils.run_query(query, '一覧')

query = '''
select *
from customer
limit 10
'''
utils.run_query(query, '一覧')

query = '''
select r.customer_id, r.amount, c.customer_name
from receipt as r inner join customer as c
on r.customer_id = c.customer_id
'''
utils.run_query(query, 'INNER JOINでくっつける')

query = '''
select r.customer_id, r.amount, c.customer_name
from receipt as r inner join customer as c
on r.customer_id = c.customer_id
where r.amount = 500
order by r.amount
'''
utils.run_query(query, 'INNER JOIN結果を条件指定する')

query = '''
select r.customer_id, r.amount, c.customer_name
from receipt as r left outer join customer as c
on r.customer_id = c.customer_id
order by r.amount
limit 100
'''
utils.run_query(query, 'LEFT OUTER JOIN、でくっつける。片方のテーブルにしかないもの出力しNullが入る。元のテーブルにない外部から情報を持ってくるので外部結合。')

query = '''
select r.customer_id, r.amount, c.customer_name
from receipt as r right outer join customer as c
on r.customer_id = c.customer_id
order by r.amount
limit 100
'''
utils.run_query(query, '↑のRIGHT OUTER JOINバージョン。customerをマスタにするのでcustomer_nameがNullにならない。')

query = '''
select c.customer_name, r.amount, p.product_cd
from customer as c left outer join receipt as r
on c.customer_id = r.customer_id
  left outer join product as p
  on r.product_cd = p.product_cd
'''

utils.run_query(query, '複数JOIN(OUTER)')

query = '''
select c.customer_name, r.amount, p.product_cd
from customer as c inner join receipt as r
on c.customer_id = r.customer_id
  inner join product as p
  on r.product_cd = p.product_cd
'''

utils.run_query(query, '複数JOIN(INNER)')

query = '''
select sales_ymd, amount, receipt_no,
  rank () over (partition by sales_ymd
    order by amount) as ranking
from receipt
limit 100
'''
utils.run_query(query, 'sales_ymdごとのamountのランキングを出す')

query = '''
select product_cd, amount,
  rank () over (order by amount) as ranking
from receipt
limit 100
'''
utils.run_query(query, '↑PARTITION BY を使わないバージョン。receiptテーブル全体でのランキングになった')

query = '''
select product_cd, amount,
  rank () over (order by amount) as ranking,
  dense_rank () over (order by amount) as dense_ranking,
  row_number () over (order by amount) as row_num
from receipt
limit 100
'''
utils.run_query(query, 'ウィンドウ専用関数でさまざまなランキング')

query = '''
select sales_ymd, amount,
  sum (amount) over (order by sales_ymd) as current_sum
from receipt
limit 100
'''
utils.run_query(query, 'ウィンドウ関数でAVG関数を使う')

query = '''
select sales_ymd, amount,
  avg (amount) over (order by sales_ymd) as current_avg
from receipt
limit 100
'''
utils.run_query(query, 'ウィンドウ関数でSUM関数を使う')

query = '''
select sales_ymd, amount,
  avg (amount) over (order by sales_ymd rows 2 preceding) as moving_avg_amount
from receipt
limit 100
'''
utils.run_query(query, '直近2つのレコードで移動平均')

query = '''
select sales_ymd, amount, receipt_no,
  rank () over (partition by sales_ymd
    order by amount) as ranking
from receipt
order by ranking
limit 100
'''
utils.run_query(query, 'グループ化された各日付ごとの順位で並び替える')
