import pandas as pd
from sqlalchemy import create_engine

host = 'database-1.c04tyndaqlxm.us-east-2.rds.amazonaws.com'
port = 5432
user = 'postgres'
password = 'postgres'
database = 'postgres'

connDB = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
conn = connDB.raw_connection()
cur = conn.cursor()

df=pd.read_sql('SELECT * FROM sales limit 10', connDB)

def get_data():
    return df
