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
    nom,lieu,pourcentage = donnee.split("-") #séparation de la chaine de charactère en plusieurs variable
    l=[nom, lieu,pourcentage] #création de la liste permetant d'ajouté des varibles au csv

    with open('test.csv', 'r', newline='') as f:
        reader = csv.reader(f)# lecture du csv
        lTot=[]
        verif=False #variable de verification 
        for row in reader:
#       Boucle permettant de verifier si la carte et deja dans le csv de modifier sa valeur sans changer l'ordre dans le csv.
            if row[0]==l[0] and row[1]==l[1]: 
                lTot.append(l) 
                verif=True
            else :
                lTot.append(row)
        if verif==False : lTot.append(l) 
    f.close()
    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(lTot) #ajout des valeurs dans le csv.
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()