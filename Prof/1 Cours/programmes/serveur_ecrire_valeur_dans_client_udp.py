# Ecrire les valeurs d'un capteur de température et d'humidité
# dans une page HTML. Déclarer un serveur HTTP. Quand ce serveur
# reçoit une requête, il renvoie dans une page HTML les valeurs du capteur
import time
import network                # module permettant la communication sur un réseau Wifi 
import socket                 # module exploitant l'outil "socket"
import gc                     # garbage collector : ramasse miettes : gestionnaire de l'espace mémoire non-utilisé
gc.collect()                  # activation du garbage collector
#import urequests as requests  #
from machine import Pin       # module de la carte ESP32
import dht                    # module pour l'utilisation du capteur de température et d'humidité

S_led = Pin(17, Pin.OUT)      # déclaration de l'objet Sortie Led
E_sensor = dht.DHT22(Pin(4))  # déclaration de l'objet Entrée Sensor

ssid = 'PA-Si-A023'           # Paramètres de notre Point d'Accès Wifi (raspberry)
password = 'wifiA023'         # mot de passe

station = network.WLAN(network.STA_IF) # création de notre station wifi ESP32
station.active(True)                   # Activation de notre station wifi sur ESP32
station.connect(ssid, password)        # tentative de connexion au Point d'Accès Wifi
while station.isconnected() == False:  # on reste dans la boucle tant que la connexion n'est pas établie 
  pass

print("Connexion au Point d'Accès Wifi établie")  # la connexion est établie
print(station.ifconfig())              # on affiche dans la console les caractéritiques IP de notre carte ESP32
print("")                              # saut d'une ligne dans l'affichage


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # création d'un objet socket
s.bind(('', 8888))                       # lier le socket à une adresse IP (ici rien = adresse de la carte) et un port (ici 80)    
  
while True:          
        contenu_requete = s.recvfrom(1024)      # on récupère de l'objet socket conn le contenu de la requête (1024 nombre de data)
        #contenu_requete = str(contenu_requete) # on le transforme en texte
        print('Contenu de la requête = %s' % contenu_requete[0])# on affiche le contenu de la requête
        print('adresse = %s' % str(contenu_requete[1]))# on affiche le contenu de la requête
        print("")                      # saut d'une ligne dans l'affichage
        E_sensor.measure()             # lance la lecture du capteur
        V_temp = E_sensor.temperature()# lecture de la température (variable de type float)
        V_hum = E_sensor.humidity()    # lecture de l'humidité (variable de type float)
        V_temp = round(V_temp, 1)      # on ne garde qu'un chiffre après la virgule
        V_hum = round(V_hum, 1)
        
        if contenu_requete[0] == b'temperature':
            s.sendto(str(V_temp),contenu_requete[1])  # envoie de la réponse
        elif contenu_requete[0] == b'humidite':
            s.sendto(str(V_hum),contenu_requete[1])  # envoie de la réponse
        elif contenu_requete[0] == b'?':
            s.sendto(str(station.ifconfig()),contenu_requete[1])  # envoie de la réponse
            s.sendto(b'8888',contenu_requete[1])    # envoie de la réponse
        else:
            s.sendto(b'Demande non reconnue',contenu_requete[1])
        time.sleep(1) # permet de ne pas saturer le DHT22
s.close()                   # on ferme l'objet socket conn
