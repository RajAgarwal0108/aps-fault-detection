import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
data_file = "/config/workspace/aps_failure_training_set1.csv"

DATABASE_NAME= "aps"
COLLECTION_NAME = "sensor"

if __name__ == '__main__':
    df = pd.read_csv(data_file)
    print(df.shape)


    # convert dataframe to json so can be dump into mongodb

    df.reset_index(drop=True,inplace=True)

    json_record =  list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)