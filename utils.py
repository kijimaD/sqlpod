import pandas as pd

# psycopg2 lets us easily run commands against our db

import psycopg2
conn = psycopg2.connect("dbname=kijima user=kijima")
conn.autocommit = True
cur = conn.cursor()

def run_command(command):
    cur.execute(command)
    return cur.statusmessage

# sqlalchemy is needed to allow pandas to seemlessly connect to run queries

from sqlalchemy import create_engine
engine = create_engine('postgresql:///kijima')

def run_query(query, description):
    print('** ' + description)
    print('#+begin_src sql')
    print(query)
    print('#+end_src')
    print(pd.read_sql_query(query,con=engine))
    return pd.read_sql_query(query,con=engine)
