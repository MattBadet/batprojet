import paho.mqtt.client as mqtt
import csv

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("niveau_gel")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    donnee=msg.payload.decode('utf-8')#Forme Nom-Lieu-Pourcentage
    print(donnee)
    nom,lieu,pourcentage = donnee.split("-")
    l=[nom, lieu,pourcentage]

    with open('bouteille.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(l)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()