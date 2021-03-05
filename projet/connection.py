import ubinascii              # module pour la conversion binaire vers ASCII et inversement
#import micropython
import network                # module permettant la communication sur un réseau Wifi 
import esp                    # module permettant d'afficher des erreurs du système d'exploitation
esp.osdebug(None)
import gc                     # garbage collector : ramasse miettes : gestionnaire de l'espace mémoire non-utilisé
gc.collect()                  # activation du garbage collector
import machine                # module complet pour la carte ESP32
from machine import Pin       # module de la carte ESP32
import dht                    # module pour l'utilisateur de ce capteur

#led = Pin(17, Pin.OUT)        # déclaration de l'objet Sortie Led
#sensor = dht.DHT22(Pin(4))    # déclarartion de l'objet Entrée sensor

ssid = 'TP-Link_D5C0'           # Paramètres de notre Point d'Accès Wifi (raspberry)
password = '15876157'         # mot de passe
mqtt_server = '192.168.0.101'  # adresse IP de notre serveur MQTT (wifi raspberry)

station = network.WLAN(network.STA_IF) # création de notre station wifi ESP32
station.active(True)                   # Activation de notre station wifi sur ESP32
station.connect(ssid, password)        # tentative de connexion au Point d'Accès Wifi
while station.isconnected() == False:  # on reste dans la boucle tant que la connexion n'est pas établie 
  pass
print("Connexion au Point d'Accès Wifi établie")  # la connexion est établie
print(station.ifconfig())              # on affiche dans la console les caractéritiques IP de notre carte ESP32
print("")                              # saut d'une ligne dans l'affichage

client_id = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()# conversion d'une donnée binaire en une représentation hexadécimal
print("adresse MAC =",client_id)     # il s'agit de l'adresse MAC de la carte ESP32 : adresse unique

sub_1 = b'niveau_gel'  # déclaration de l'intitulé du sujet 1 : b' indique une chaine de caractères sous forme d'octets

dernier_message = 0                    # initialisation d'une variable utilisée pour la gestion du temps
interval_entre_message = 5             # variable permettant d'attendre 5 seconde pour réalliser une nouvelle mesure de capteur
compteur = 0                           # initialisation d'un compteur

def connexion():
    global client_id, mqtt_server     # identification des variables globales
    client = MQTTClient(client_id, mqtt_server)   # création d'un objet client MQTT
    client.connect()                              # connexion entre le client et le serveur
    print('Connexion au %s le MQTT broker' % mqtt_server)# affichage de l'adresse IP du serveur MQTT
    return client                     # renvoie du client MQTT

def restart_et_reconnexion():          # fonction permettant une réinitialisation en cas de problème de connexion
    print('Problème de connexion au broker MQTT. Re-connexion en cours ...')
    time.sleep(10)
    machine.reset()

try:
    client = connexion()           # appel à la fonction créant l'objet client MQTT
except OSError as e:             # si une erreur du type OSError sur vient on afiche "erreur 1"
    print("erreur 1")  
    restart_et_reconnexion()      # appel à la fonction de réinitialisation
    
while True:           # La boucle infinie : programme principal
    try:        
        if (time.time() - dernier_message) > interval_entre_message:# si on a dépasser une durée définie par message_interval
            compteur += 1                # on incrémente un compteur
            print("compteur =",compteur)  # affichage de la valeur du compteur
            
            msg = input("envoyer :")             # on transforme un float en str
            #msg = msg.encode('utf-8')   # on transforme la variable str utf-8 en variable de type tableau d'octets
            #print(type(msg),"msg = ",msg)   # affichage du type et du contenu de la variable
            client.publish(sub_1,msg)# le client MQTT publie son message à propos du sujet "temperature"
                                        # cette publication est envoyée au serveur MQTT c'est à dire au raspberry           
                        
            dernier_message = time.time()  # on mesure à nouveau le temps qui s'est écoulé depuis le démarrage de la carte

    except OSError as e:            # si message d'erreur du type OSError alors on redémarre la carte
        restart_et_reconnexion()
