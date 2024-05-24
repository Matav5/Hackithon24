import paho.mqtt.client as mqtt
import ssl
import os
import json
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import pymongo
from datetime import datetime
load_dotenv()

messages = 0
troughput = 0

messages_per_minute = 0
troughput_per_minute = 0

mongo_user = os.getenv("mongo_user")
mongo_password = os.getenv("mongo_password")
mongo_host = os.getenv("mongo_host")
mongo_port = os.getenv("mongo_port")
client = pymongo.MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["portabo"]
collection = db["portabo"]


def every_second():
    global messages, troughput, messages_per_minute, troughput_per_minute
    print(f"Zprav za sekundu: {messages}, Datovy tok: {troughput} B/s")
    messages_per_minute += messages
    troughput_per_minute += troughput
    messages = 0
    troughput = 0


def every_minute():
    global messages_per_minute, troughput_per_minute
    print(f"Zprav za minutu: {messages_per_minute}, Datovy tok: {troughput_per_minute / 1024} kB/s,")
    print()
    messages_per_minute = 0
    troughput_per_minute = 0


scheduler = BackgroundScheduler()
scheduler.add_job(every_second, 'interval', seconds=1)
scheduler.add_job(every_minute, 'interval', minutes=1)
scheduler.start()


broker_address = "mqtt.portabo.cz"
port = 8883
mqtt_user = os.getenv("mqtt_user")
mqtt_password = os.getenv("mqtt_password")


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("#")


def on_message(client, userdata, msg):
    global messages, troughput
    messages += 1
    troughput += len(msg.payload)
   
    try:
        # Include all attributes from msg into the MongoDB document
        current_dateTime = datetime.now()
        message = {
            "topic": msg.topic,
            "payload": json.loads(msg.payload.decode()),
            "dup": msg.dup,
            "mid": msg.mid,
            "properties": msg.properties,
            "qos": msg.qos,
            "retain": msg.retain,
            "state": msg.state,
            "timestamp": current_dateTime
        }
        collection.insert_one(message)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if "senzory" in msg.topic:
        print(f"{msg.payload.decode()}")
   # print(f"{msg.payload.decode()}")
    #print(f"Message received: Topic: {msg.topic}")


client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_password)
client.on_connect = on_connect
client.on_message = on_message

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE
client.tls_set_context(ssl_ctx)
client.tls_insecure_set(True)


client.connect(broker_address, port, 60)

client.loop_forever()
