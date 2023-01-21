import pandas as pd
import pymongo
import json
from dataclasses import dataclass
import os,sys
#provide the mongoDB localhost url to connect python to mongodb


class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")



env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)