# Programme permettant de recevoir des messages de la part d'un serveur MQTT
# avec un plusieurs abonnements à des sujets différents

import time                   # module pour la gestion du temps
from umqttsimple import MQTTClient # module pour l'utilisation de MQTT pour un CLIENT
import ubinascii              # module pour la conversion binaire vers ASCII et inversement
#import micropython
import network                # module permettant la communication sur un réseau Wifi 
import esp                    # module permettant d'afficher des erreurs du système d'exploitation
esp.osdebug(None)
import gc                     # garbage collector : ramasse miettes : gestionnaire de l'espace mémoire non-utilisé
gc.collect()                  # activation du garbage collector
import machine                # module complet pour la carte ESP32
from machine import Pin       # module de la carte ESP32

ssid = 'WIFI_A023'           # Paramètres de notre Point d'Accès Wifi (raspberry)
password = 'ADMINA023'         # mot de passe
mqtt_server = '10.121.44.47'  # adresse IP de notre serveur MQTT (wifi raspberry)

station = network.WLAN(network.STA_IF) # création de notre station wifi ESP32
station.active(True)                   # Activation de notre station wifi sur ESP32
station.connect(ssid, password)        # tentative de connexion au Point d'Accès Wifi
while station.isconnected() == False:  # on reste dans la boucle tant que la connexion n'est pas établie 
  pass
print("Connexion au Point d'Accès Wifi établie")  # la connexion est établie
print(station.ifconfig())              # on affiche dans la console les caractéritiques IP de notre carte ESP32
print("")                              # saut d'une ligne dans l'affichage

client_id = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()# conversion d'une donnée binaire en une représentation hexadécimal
print("mac",client_id)
sujet_abonnement_1 = b'temperature'
sujet_abonnement_2 = b'humidite'
last_message = 0
message_interval = 5
counter = 0

def sub_cb(sujet, msg):
    """ fonction de rappel qui gère ce qu'on doit faire à la réception d'une publication
    concernant un sujet pour lequel la carte ESP32-2 s'est abonnée
    Elle reçoit comme paramètres :
    - le sujet : variable de type str
    - le message : variable de type str """
    msg=msg.decode('utf-8')                           # transforme la variable tableau d'octets en chaîne de caractères
    if sujet == b'temperature':        
        print("La température a éteint la valeur de {}°C".format(msg))
    elif sujet == b'humidite':
        print("L'humidité est de {}%".format(msg))

def connexion_et_abonnement():
    global client_id, mqtt_server, sujet_abonnement_1, sujet_abonnement_2# déclaration de l'utilisation de variables globales
    client = MQTTClient(client_id, mqtt_server)   # création d'un objet client MQTT
    client.set_callback(sub_cb)                   # création d'une fonction de rappel pour le client MQTT
    client.connect()                              # connexion entre le client et le serveur
    client.subscribe(sujet_abonnement_1)          # Pour l'objet client MQTT, on souscrit un abonnement à propos du sujet : ici "temperature"
    print('Connexion au %s le MQTT broker, Abonné au sujet %s' % (mqtt_server, sujet_abonnement_1))
    client.subscribe(sujet_abonnement_2)          # Pour l'objet client MQTT, on souscrit un abonnement à propos du sujet : ici "temperature"
    print('Connexion au %s le MQTT broker, Abonné au sujet %s' % (mqtt_server, sujet_abonnement_2))

    return client

def restart_et_reconnexion():
    print('Problème de connexion au broker MQTT. Re-connexion en cours ...')
    time.sleep(10)
    machine.reset()

try:
    client = connexion_et_abonnement()
except OSError as e:
    print("error 1")  
    restart_et_reconnexion()

while True:
    try:        
        test = client.check_msg() # méthode qui vérifie si un message et disponnible sur le serveur MQTT pour notre client MQTT
                           # si un message est disponible concerant le sujet (ici "temperature), on déclenche la fonction
                           # sub_cb qui gère la réception et le fonctionnement à tenir en concéquence        
    
    except OSError as e:
        restart_et_reconnexion()
