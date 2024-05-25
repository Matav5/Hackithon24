import pandas as pd
import pymongo as pm
from datetime import datetime, timezone, timedelta
import zpracovani

client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
collection_hourlytopic = db["topic_za_hodinu"]
collection_sensors = db['portabo']
collection_category_troughput = db['category_troughput']

def parse_mongo_data_by_hourlytopic():
    # Načtení dat z MongoDB
    data_list = list(collection_hourlytopic.find())
        
    # Příprava datového rámce s explicitním rozbalením vnořených slovníků
    data_frame = pd.DataFrame(data_list)
    topics = (data_frame['_id'].apply(lambda x: x['topic']).tolist(), data_frame['count'].tolist())
        
    # Použití funkce clean_topics na celý DataFrame
    topic_counts = clean_topics(data_frame)
        
    return topics, topic_counts


def clean_topics(data):
    def format_topic(topic):
        topic = topic.lower()  # Normalizace na malá písmena pro konzistentní porovnání
        if '/bilina/kamery' in topic:
            return 'Kamery Bílina'
        elif 'ttndata' in topic:
            return 'TTN'
        elif 'udp' in topic:
            return 'UDP'
        elif '/voda/' in topic:
            return 'Voda KA'
        elif '/vodomery/' in topic:
            return 'Vodoměry Děčín'
        elif '/senzory/wifi' in topic:
            return 'WiFi Senzory'
        elif '/mve/' in topic:
            return 'Vodní Elektrárna'
        elif '/povodnova-cidla' in topic:
            return 'Povodnová Čidla'
        else:
            return 'Other'

    # Vytvoření nového sloupce 'cleaned_topic' s upravenými topicy
    data['cleaned_topic'] = data['topic'].apply(lambda x: format_topic(x))

    # Počítání výskytů jednotlivých témat
    topic_counts = data.groupby('cleaned_topic').size().to_dict()

    return topic_counts

def update_troughput_per_minute():
    # Aktuální čas a čas před minutou
    current_time = datetime.now(timezone.utc)
    one_minute_ago = current_time - timedelta(minutes=1)
        
    # Načtení dat z MongoDB pro průtoková data za poslední minutu
    data = list(collection_sensors.find({"timestamp": {"$gte": one_minute_ago, "$lte": current_time}}))
        
    if data:
        # Příprava datového rámce
        df = pd.DataFrame(data)
        # Použití funkce clean_topics na data
        topic_counts = clean_topics(df)
        return topic_counts
    else:
        return "No data found for the last minute."


# Zavolání funkce a vypsání výsledků
topics_last_minute = update_troughput_per_minute()
print(topics_last_minute)
