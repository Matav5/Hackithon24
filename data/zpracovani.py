#Zde by mělo proběhnout načtení a zpracování dat ze
# kterých budou čerpat gray.py
import pandas as pd
import pymongo as pm
from datetime import datetime, timedelta,timezone
import pipeliny
client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
collection = db["portabo"]

    
def get_topics():
    data_list = list(collection.aggregate(pipeliny.branchesPipeline()))
    data_list = [item['_id'] for item in data_list]
    return data_list
 
def get_topic(nazev,od=None ,do=None):
    ls =list()
    for item in pipeliny.topicPipeline(nazev):
        ls.append(item)
    for item in time_filter(od, do):
        ls.append(item)
    print(ls)
    
    data_list = list(collection.aggregate(ls))
    return data_list
    
def time_filter(od, do=None):
    if od is None:
        return []
    if do is None:
       do = datetime.now(timezone.utc) 
    pipeline = [
        {
            '$match': {
                'timestamp': {
                    '$gte': od,
                    '$lte': do
                }
            }
        }
    ]
    return pipeline


def get_cetnosti(od=None, do=None):
    ls = list()
    for item in time_filter(od, do):
        ls.append(item)
    for item in pipeliny.cetnostiPipeline():
        ls.append(item)    
    data_list = list(collection.aggregate(ls))
    df = pd.DataFrame(data_list)
    df.rename(columns={'_id': 'nazev'}, inplace=True)
    return df
#vycistit zdokumenetovat, udělat četnosti, devops

if __name__ == "__main__":
    print(get_topics());
    print(get_cetnosti());
  #  print(get_topic("/Bilina",datetime(2024,5,24,22),datetime(2024,5,24,22,5)));