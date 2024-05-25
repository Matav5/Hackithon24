import zpracovani
import pandas as pd
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize an empty DataFrame to store topics over time
cached_topics_df = pd.DataFrame(columns=['timestamp', 'retain', 'qos', 'dup', 'payload_state', 'payload_properties', 'topic', 'mid', '_id'])

def cache_topics_every_minute():
    global cached_topics_df
    current_time = datetime.now()
    one_minute_ago = current_time - timedelta(minutes=1)
    
    topics = zpracovani.get_topics()
    
    # Fetch data for each topic from the last minute
    for topic in topics:
        topic_data = zpracovani.get_topic(topic, one_minute_ago, current_time)
        if topic_data:
            for data in topic_data:
                # Append each topic data to the DataFrame
                cached_topics_df = cached_topics_df.append({
                    'timestamp': data['timestamp'],
                    'retain': data['retain'],
                    'qos': data['qos'],
                    'dup': data['dup'],
                    'payload_state': data['payload']['state'],
                    'payload_properties': data['payload']['properties'],
                    'topic': data['topic'],
                    'mid': data['mid'],
                    '_id': data['_id']
                }, ignore_index=True)
            print(cached_topics_df)
            

# Schedule the caching function to run every minute
cache_topics_every_minute()
scheduler = BackgroundScheduler()
scheduler.add_job(cache_topics_every_minute, 'interval', minutes=1)
scheduler.start()
