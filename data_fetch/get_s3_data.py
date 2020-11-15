import boto3
import botocore
from botocore import UNSIGNED
from botocore.config import Config
import pandas as pd
import os

BUCKET_NAME = os.environ['BUCKET_NAME']

def get_s3_matrix(city):
    '''
    This functions consults the s3 AWS bucket and returns
    a csv of the city that is required. The csv is returned
    as a pandas Dataframe
    params: 
        - city : city to be consulted in the s3 AWS
    returns:
        - csv of the city as a dataframe
    '''

    path = 'distances/{}.csv'.format(city)
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    name = '{}.csv'.format(city)
    try:
        
        s3.Bucket(BUCKET_NAME).download_file(path, name)
        df_recoms = pd.read_csv(name)
        os.remove(name)
    except botocore.exceptions.ClientError as e: 
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.", e)
        else:
            raise
    return df_recoms
