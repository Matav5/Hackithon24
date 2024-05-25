#Zde by mělo proběhnout načtení a zpracování dat ze
# kterých budou čerpat gray.py
import pandas as pd
import pymongo as pm
from datetime import datetime, timedelta,timezone

client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
collection = db["portabo"]
regex_then_dict = {
    "^/ttndata": "/ttndata",
    "^/vodomery": "/vodomery",
    "^/Bilina": "/Bilina",
    "^/senzory": "/senzory",
    "^/mve": "/mve",
    "^/voda": "/voda",
    "^/udp1881": "/udp1881"
}
default_pipeline= []


branches = [
    {"case": {"$regexMatch": {"input": "$topic", "regex": regex}}, "then": then} for regex, then in regex_then_dict.items()
]

def branchesPipeline():
    pipeline = [
        {
            "$set": {
                "general_topic": {
                    "$switch": {
                        "branches": branches,
                        "default": "$topic"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$general_topic"
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]
    return pipeline


def topicPipeline(nazev):
    topicPipeline = [
        {
            "$set": {
            "general_topic": {
                "$switch": {
                "branches": branches,
                "default": "$topic"
                }
            }
            }
        },
        {
            "$match": { "general_topic": nazev }
        },
        {
            "$sort": { "_id": 1 }
        }
    ]
        
    return topicPipeline
   
   
   
   
def get_topics():
    data_list = list(collection.aggregate(branchesPipeline()))
    data_list = [item['_id'] for item in data_list]
    return data_list

 
def get_topic(nazev,od=None ,do=None):
    ls =list()
    for item in topicPipeline(nazev):
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


#print(get_topics());
#print(get_topic("/Bilina",datetime(2024,5,24),datetime(2024,5,25)));