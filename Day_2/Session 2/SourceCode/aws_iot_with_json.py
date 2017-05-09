#!/usr/bin/python3

#required libraries
import sys 
import ssl
import paho.mqtt.client as mqtt
import time
from time import sleep
import json

source_bus_entry = {}
source_bus_entry['id'] = 'value'
source_bus_entry['bus_entry_time'] = 'value'
source_bus_entry['bus_source'] = 'value'
source_bus_entry['bus_destination'] = 'value'
source_bus_entry['bus_no'] = 'value'
source_bus_entry['bus_time'] = 'value'
source_bus_entry['source_train_time'] = 'value'
source_bus_entry['train_source'] = 'value'
source_bus_entry['source_bus_stop_name'] = 'value'


json_source_bus_entry = json.dumps(source_bus_entry)

#called while client tries to establish connection with the server
def on_connect(mqttc, obj, flags, rc):
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

#called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))

#called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

#creating a client with client-id=mqtt-test
mqttc = mqtt.Client(client_id="MyBus")

mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

#Configure network encryption and authentication options. Enables SSL/TLS support.
#adding client-side certificates and enabling tlsv1.2 support as required by aws-iot service
mqttc.tls_set("rootCA.crt",
certfile="9bf9f3f659-certificate.pem.crt",
keyfile="9bf9f3f659-private.pem.key",
tls_version=ssl.PROTOCOL_TLSv1_2,
ciphers=None)

#connecting to aws-account-specific-iot-endpoint
mqttc.connect("a1hdhui1ajdqbv.iot.ap-southeast-1.amazonaws.com", port=8883) #AWS IoT service hostname and portno
time.sleep(20)
#the topic to publish to
#mqttc.subscribe("CaptureSensorDataPolicy", qos=0) #The names of these topics start with $aws/things/thingName/shadow."

mqttc.loop_start()

#automatically handles reconnecting
#mqttc.loop_forever()

mqttc.publish("MyBusPolicy", json_source_bus_entry, 0)
        
