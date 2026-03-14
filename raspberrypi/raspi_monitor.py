import paho.mqtt.client as mqtt
import json
import requests
from datetime import datetime

# GOOGLE SHEETS WEB APP URL
url = "PASTE_YOUR_GOOGLE_SCRIPT_URL_HERE"

# Patient age data
ages = {
"Aarav Sharma":22,
"Diya Patel":21,
"Rohan Verma":23,
"Ananya Reddy":22,
"Vikram Singh":24,
"Meera Nair":21,
"Rahul Das":23,
"Kavya Iyer":22,
"Arjun Mehta":24,
"Sneha Kulkarni":21
}

# MQTT SETTINGS
broker = "broker.hivemq.com"
topic = "healthband/data"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(topic)

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    name = data["name"]
    heart_rate = data["heart_rate"]
    temperature = data["temperature"]

    print(name, heart_rate, temperature)

    # Save to local file
    with open("healthdata.txt","a") as f:
        f.write(f"{datetime.now()} {name} {heart_rate} {temperature}\n")

    # Determine alert
    alert_flag = 0

    if heart_rate > 120 or temperature > 37.8:
        alert_flag = 1
        print("ALERT:", name)

    age = ages[name]

    # Send to Google Sheets
    params = {
        "name": name,
        "age": age,
        "temp": temperature,
        "heart": heart_rate,
        "alert": alert_flag
    }

    try:
        requests.get(url, params=params)
    except:
        print("Error sending data to Google Sheets")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker,1883,60)

client.loop_forever()
