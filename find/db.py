import os
from pymongo import MongoClient

mongo_client = MongoClient(os.environ['database'])


