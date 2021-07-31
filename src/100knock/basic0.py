import utils_k as utils

print('* ' + 'データだけ流用して、中身は基本的なクエリの練習')

query = '''
select *
from receipt
limit 10
'''
utils.run_query(query, '内容確認する')

query = '''
select store_cd, amount
from receipt as s1
where amount > (select AVG(amount)
                from receipt as s2
                where s1.store_cd = s2.store_cd
                group by store_cd)
limit 10
'''
utils.run_query(query, '相関サブクエリ。強引に置き換えたため集計内容に意味はない')

query = '''
select store_cd, AVG(amount)
from receipt
group by store_cd
limit 10
'''
utils.run_query(query, '相関サブクエリの中身を見てみる')

query = '''
select distinct product_cd, amount
from receipt
where amount
in (158, 81, 30)
limit 10
'''
utils.run_query(query, 'IN述語で複数条件')

query = '''
select amount, quantity
from receipt
where quantity
not in (1, 3)
limit 10
'''
utils.run_query(query, 'NOT IN')

query = '''
select store_cd, amount, product_cd, customer_id
from receipt
where customer_id in (
  select customer_id
  from receipt
  where product_cd = 'P070305012')
limit 10
'''
utils.run_query(query, 'サブクエリで条件検索する')

query = '''
select customer_id, product_cd
from receipt
where product_cd = 'P070305012'
limit 10
'''
utils.run_query(query, '↑サブクエリの中身')

query = '''
select store_cd, receipt_no, amount
from receipt as r0
where exists (
  select *
  from  receipt as r1
  where r1.amount = 158
  and r0.sales_ymd = r1.sales_ymd)
limit 10
'''
utils.run_query(query, 'EXISTS関数。あまりうまい例が思いつかなかった')

query = '''
select receipt_no,
  case when store_cd = 'S14006'
       then '大阪:' || store_cd
       when store_cd = 'S13008'
       then '鳥取' || store_cd
       when store_cd = 'S14028'
       then '名古屋' || store_cd
       else null
     end as store
from receipt
limit 10
'''
utils.run_query(query, 'WHENで文字を挿入する')

query = '''
select
  sum(case when store_cd = 'S14006'
    then receipt_no else 0 end) as sum_14,
  sum(case when store_cd = 'S13008'
    then receipt_no else 0 end) as sum_15,
  sum(case when store_cd = 'S14028'
    then receipt_no else 0 end) as sum_16
from receipt
'''
utils.run_query(query, '集計した内容を行列変換する')

query = '''
select store_cd, amount
from receipt
where amount < 300
union
select store_cd, amount
from receipt
where amount < 350
order by amount
'''
utils.run_query(query, 'UNIONでくっつける')

query = '''
select store_cd, amount
from receipt
where amount < 300
intersect
select store_cd, amount
from receipt
where amount < 350
order by amount
'''
utils.run_query(query, 'INTERSECTで共通部分')

query = '''
select store_cd, amount
from receipt
where amount < 300
intersect all
select store_cd, amount
from receipt
where amount < 350
order by amount
'''
utils.run_query(query, 'ALLで重複を削除しない')

query = '''
select store_cd, amount
from receipt
where amount < 350
except
select store_cd, amount
from receipt
where amount < 300
order by amount
'''
utils.run_query(query, 'EXCEPTで引き算。350以下から300以下を引く。なので300以下は含まれていない')
