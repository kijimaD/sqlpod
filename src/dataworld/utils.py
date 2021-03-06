import sqlparse
import pandas as pd

# psycopg2 lets us easily run commands against our db

import psycopg2
conn = psycopg2.connect("dbname=kijima user=kijima")
conn.autocommit = True
cur = conn.cursor()

def run_command(command, description):
    print('** ' + description + '(command)')
    print('#+begin_src sql')
    print(sqlparse.format(command, reindent=True, keyword_case='upper'))
    print('#+end_src')
    try:
        cur.execute(command)
    except:
        pass

# sqlalchemy is needed to allow pandas to seemlessly connect to run queries
from sqlalchemy import create_engine
engine = create_engine('postgresql:///kijima')

def run_query(query, description):
    print('** ' + description)
    print('#+begin_src sql')
    print(sqlparse.format(query, reindent=True, keyword_case='upper'))
    print('#+end_src')
    print()
    print('#+begin_src')
    print(pd.read_sql_query(query,con=engine))
    print('#+end_src')
    return pd.read_sql_query(query,con=engine)
