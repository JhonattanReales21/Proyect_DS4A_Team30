import pandas as pd
from sqlalchemy import create_engine
from os import environ
from data_fetch.unpivoting import sub_pivots

DB_URI = environ['URI']
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
        select * from {0}
    """.format(view_name)
    return pd.read_sql_query(query, con=ENGINE)


def get_cosine_views(city):
    """
    This function is intended to fetch the cosine_similarity of article types in a city 
    in a matrix representation.
    params:
        - city: city to filter
    return:
        :pd.Dataframe containing the cosine similarity as a Matrix Representation
    """
    query = """
        select * from cosine_similarity where city = '{0}'
    """.format(city)
    data = pd.read_sql_query(query, con=ENGINE)

    return sub_pivots(data, 'tipo_articulo_1', 'tipo_articulo_2', 'cosine_similarity')
