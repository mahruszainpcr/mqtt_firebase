import time
import paho.mqtt.client as mqtt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('iot_mikro.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://firebaseio.com/'
})

ref = db.reference('/')
ref.set({
        'labjti': 
            {
                '320': {
                    'Lampu': 'On',
                    'Suhu': 28
                },
                '319': {
                    'Lampu': 'On',
                    'Suhu': 28
                },
                '325': { 
                    'Lampu': 'Off',
                    'Suhu': 30
                }
            }
        })
# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("building/lampu")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    value=str(msg.payload)
    ref = db.reference('labjti')
    box_ref = ref.child('320')
    box_ref.update({
        'Lampu': value[2:-1]
    })
    print ( msg.topic+" "+value[2:-1] )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)


# client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    # client.publish("building/lampu","Getting Started with MQTT")
    # print ("Message Sent")
    time.sleep(1)

client.loop_stop()
client.disconnect()