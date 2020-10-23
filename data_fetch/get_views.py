import pandas as pd
from sqlalchemy import create_engine

DB_URI = 'postgres://postgres:postgres@database-1.c04tyndaqlxm.us-east-2.rds.amazonaws.com:5432/postgres'
ENGINE = create_engine(DB_URI)

def get_view_by_name(view_name):
    """
    This function is intended to fetch a whole (materialized) view/table data into a pd.Dataframe
    params:
        - view_name: name of the SQL relation to fetch. :type str
    return:
        :pd.Dataframe containing with all the data fetched from the SQL relation.
    """
    query = """
        select * {0}
    """.format(view_name)
    return pd.read_sql_query('select * from venta_ciudad_tienda', con=ENGINE)