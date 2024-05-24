import pandas as pd
import pymongo as pm
from datetime import datetime, timedelta
client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
throughput_per_minute_collection = db["throughput_per_minute"]

def throughput_per_minute(days=1):
    time_threshold = datetime.utcnow() - timedelta(days=days)
    print(time_threshold)


    data_list = list(throughput_per_minute_collection.find({"_id": {"$gte": str(time_threshold).replace(" ", "T")}}))
    data_frame = pd.DataFrame(data_list)
    return data_frame
#data_frame['hour'] = data_frame[0].apply(lambda x: x['hour'])
#data_frame['topic'] = data_frame[0].apply(lambda x: x['topic'])

print(throughput_per_minute().head())
