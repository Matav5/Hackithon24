import zpracovani
import pandas as pd
import pymongo as pm
from datetime import datetime, timezone, timedelta

client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
collection_hourlytopic = db["topic_za_hodinu"]
collection_sensors = db['portabo']
collection_category_troughput = db['category_troughput']


def parse_mongo_data_by_hourlytopic():
    # Načtení dat z MongoDB
    data_list = list(collection_hourlytopic.find())

    # Příprava datového rámce s explicitním rozbalením vnořench slovníků
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
        elif '/vodomery/' or '/voda' in topic:
            return 'Vodoměry Děčín'
        elif '/senzory/wifi' in topic:
            return 'WiFi Senzory'
        elif '/mve/' in topic:
            return 'Vodní Elektrárna'
        elif '/povodnova-cidla' in topic:
            return 'Povodnová Čidla'
        else:
            return 'Other'

    # Vytvoření nového sloupce 'cleaned_topic' s upravenmi topicy
    data['cleaned_topic'] = data['_id'].apply(lambda x: format_topic(x['topic']))

    # Počítání výskytů jednotlivých témat
    topic_counts = data.groupby('cleaned_topic')['count'].sum().to_dict()

    return topic_counts


def update_troughput_per_minute():
    # Načtení dat z MongoDB pro průtoková data
    topics = zpracovani.get_topics()
    
    current_time = datetime.now(timezone.utc)
    one_minute_ago = current_time - timedelta(minutes=10)
    for topic in topics:
        actual = zpracovani.get_topic(topic, one_minute_ago, current_time)
        clean = clean_topics(actual)
        print(clean)
    
    # Získání dat z kolekce
    data = list(collection_category_troughput.find(query))
    
    # Příprava datového rámce
    if data:
        df = pd.DataFrame(data)
        # Agregace dat podle kategorie a výpočet sumy průtoků
        result = df.groupby('category')['troughput'].sum().reset_index()
        
        # Aktualizace MongoDB s novými agregovanými daty
        for index, row in result.iterrows():
            collection_category_troughput.update_one(
                {"category": row['category']},
                {"$set": {"last_minute_troughput": row['troughput']}},
                upsert=True
            )
    else:
        print("No data found for the last minute.")



parse_mongo_data_by_hourlytopic()
update_troughput_per_minute()

