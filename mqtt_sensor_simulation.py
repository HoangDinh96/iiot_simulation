import paho.mqtt.client as mqtt
import random
import time

# MQTT Broker details
broker = "localhost"
port = 1883
topic = "sensor/data"

# Function to simulate sensor data and publish to MQTT broker
def simulate_sensor_data():
    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
        client.publish(topic, payload)
        print(f"Published: {payload} to topic {topic}")  # Optional: Debugging message
        time.sleep(1)

# Initialize MQTT Client
client = mqtt.Client()
client.connect(broker, port)

# Start publishing sensor data
simulate_sensor_data()