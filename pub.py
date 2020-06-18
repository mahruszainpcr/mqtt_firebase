import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import paho.mqtt.client as mqtt

# Fetch the service account key JSON file contents
cred = credentials.Certificate('iot_mikro.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mikro-b4844.firebaseio.com/'
})

ref = db.reference('lampu')
print(ref.get())
i=0
while True:
    print(ref.get())
    if ref.get()=="Off" and i==0 :
        i=1
        client = mqtt.Client()
        client.connect("127.0.0.1",1883,60)
        client.publish("building/lampu", "Off")
    if ref.get()=="On"  and i==1 :
        i=0
        client = mqtt.Client()
        client.connect("127.0.0.1",1883,60)
        client.publish("building/lampu", "On")
# client.disconnect();
        