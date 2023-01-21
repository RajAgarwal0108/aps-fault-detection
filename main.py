from sensor.utils import get_collection_names
from sensor.exception import SensorException
import os,sys

if __name__ == "__main__":
    try:
        df = get_collection_names(database_name="aps", collection_name="sensor")
        print(df.columns)
    except Exception as e:
        raise SensorException(e,sys)