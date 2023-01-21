import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys

def get_collection_names(database_name:str,collection_name:str)->pd.DataFrame():
    """
    This function return collecion as DataFrame
    datbase_name : database name
    collection_name : collection name
    ===========================================

    return Pandas dataframe of a collection

    """

    try:
        logging.info(f"Reading Data From Database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"found columns:{df.columns}")
        if "_id" in df.columns:
            logging.info("droping column '_id' from DataFrame")
            df = df.drop('_id',axis=1)
        logging.info(f"Rows and Columns in df:{df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)