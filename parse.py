import pandas as pd
import pymongo as pm

client = pm.MongoClient("mongodb://matav:Nevim123@167.86.71.184:27017/")
db = client["portabo"]
collection_hourlytopic = db["topic_za_hodinu"]


def parse_mongo_data_by_hourlytopic(data):
    if 'topic' in data.columns:
        # Agregace dat podle tématu a výpočet průměrných hodnot pro ostatní sloupce
        aggregated_data = data.groupby('topic').mean()
        print(aggregated_data)
        return aggregated_data
    else:
        return pd.DataFrame()

def categorize_messages(data):
    if 'topic' in data.columns:
        categorized_data = data.groupby('topic').apply(lambda x: x)
        return categorized_data
    else:
        return pd.DataFrame()

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
        return topic

    # Vytvoření nového sloupce 'cleaned_topic' s upravenými topicy
    data['cleaned_topic'] = data['_id'].apply(lambda x: format_topic(x['topic']))

    return data

# Načtení dat z MongoDB
data_list = list(collection_hourlytopic.find())

# Příprava datového rámce s explicitním rozbalením vnořených slovníků
data_frame = pd.DataFrame(data_list)
#data_frame['hour'] = data_frame[0].apply(lambda x: x['hour'])
#data_frame['topic'] = data_frame[0].apply(lambda x: x['topic'])

print(data_frame[:5])
data_frame[:5].to_csv('first_five_items.txt', sep='\t', index=False)
topics = data_frame['_id'].apply(lambda x: x['topic']).tolist()

print(topics)  # Vypíše seznam topiců
#parse_mongo_data_by_hourlytopic(data_frame)

# Použití funkce clean_topics na celý DataFrame
data_frame = clean_topics(data_frame)
print(data_frame[['cleaned_topic']])  # Vypíše nový sloupec s upravenými topicy
