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

def sensorsPipeline():
    pipe = [
        {
            '$match': {
                'payload.sensor': {
                    '$exists': True, 
                    '$ne': None
                }
            }
        }, {
            '$group': {
                '_id': None, 
                'sensors': {
                    '$addToSet': '$payload.sensor'
                }
            }
        }, {
            '$unwind': '$sensors'
        }, {
            '$sort': {
                'sensors': 1
            }
        }, {
            '$project': {
                '_id': 0, 
                'sensor': '$sensors'
            }
        }
    ]
    return pipe
def sensorPipeline():
    pipe = [
        {
            '$match': {
                'payload.sensor': 'BI-MO-I1'
            }
        }, {
            '$sort': {
                'timestamp': 1
            }
        }
    ]
    return pipe
   
def detectionPipeline():
    pipe = [
    {
        '$match': {
            'payload.detectionType': {
                '$exists': True, 
                '$ne': None
            }
        }
    }, {
        '$group': {
            '_id': None, 
            'detectionType': {
                '$addToSet': '$payload.detectionType'
            }
        }
    }, {
        '$unwind': '$detectionType'
    }, {
        '$sort': {
            'detectionType': 1
        }
    }, {
        '$project': {
            '_id': 0, 
            'detectionType': '$detectionType'
        }
    }
]
    return pipe
def matchDetectionPipeline():
    pipe = [
    {
        '$match': {
            'payload.detectionType': 'detector'
        }
    }, {
        '$sort': {
            'timestamp': 1
        }
    }
]  
    return pipe
