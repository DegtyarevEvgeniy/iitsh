import sqlite3

import random

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "Dev"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = ''
password = ''


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def pas_data_to_bd(arr):

    base = sqlite3.connect("db.sqlite3")

    cur = base.cursor()

#     arr = ['1', '001', '10:00:00', '0', '24', '57', '750', '20', '600', '0', '1', '0']


    cur.execute("INSERT INTO cloud_cabinet VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (int(arr[0]), arr[1], arr[2], '0', arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], '0', arr[10], arr[11]))
    base.commit()


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        main_str = msg.payload.decode()
        arr = str(main_str).split()
        print(arr)
        pas_data_to_bd(arr)
        
            

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
    

# mac=00:00:00:00:00:00;cabinet= 001; time=10:00:00;alarm=0;temperature=24;humidity=57;pressure=750;lux=20;co2=600;co=0;movement=1;door=0
