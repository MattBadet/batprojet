# Quand clique sur BP ON on allume une led
# Quand clique sur BP OFF on éteint une led

import network                # module permettant la communication sur un réseau Wifi 
import socket                 # module exploitant l'outil "socket"
import gc                     # garbage collector : ramasse miettes : gestionnaire de l'espace mémoire non-utilisé
gc.collect()                  # activation du garbage collector
#import urequests as requests  #
from machine import Pin       # module de la carte ESP32

led = Pin(17, Pin.OUT)

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

V_html = """<!doctype html><html lang="fr"><head><meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Réponse du serveur</title></head><body><h1>ESP Web Server</h1><a href="?led=on\"><button>ON</button>
        </a>&nbsp;<a href="?led=off\"><button>OFF</button></a></body></html>"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # création d'un objet socket
s.bind(('', 80))                       # lier le socket à une adresse IP (ici rien = adresse de la carte) et un port (ici 80)
s.listen(5)                            # le socket est prêt à écouter (5 communications maxi en même temps)

while True:
    conn, addr = s.accept()      # le socket "s" attend une demande. Quand la requête arrive
                                 # conn est un nouvel objet socket qui sert pour recevoir ou envoyer la donnée
                                 # addr variable qui contient l'adresse IP du client ayant envoyé la requête  
    print('Connexion établie avec %s' % str(addr)) # affichage de l'adresse IP du client
    print("")
    contenu_requete = conn.recv(1024)      # on récupère de l'objet socket conn le contenu de la requête (1024 nombre de data)
    contenu_requete = str(contenu_requete) # on le transforme en texte
    print('CONTENU DE LA REQUETE = %s' % contenu_requete)# on affiche le contenu de la requête
    print("")                      # saut d'une ligne dans l'affichage
    indice_led_on = contenu_requete.find('?led=on')  # récupération de l'indice où se trouve le mot "?led=on"
    indice_led_off = contenu_requete.find('?led=off')# récupération de l'indice où se trouve le mot "?led=off"
    if indice_led_on == 7:
        print('LED ON')
        led.value(1)
    if indice_led_off == 7:
        print('LED OFF')
        led.value(0)
    V_reponse_complete='HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n'+V_html
    print("REPONSE COMPLETE :",V_reponse_complete) # affichage de la trame HTTP envoyé comme réponse
    conn.sendall(V_reponse_complete)                  # réponse envoyée : ici le contenu HTML toujours identique 
    conn.close()
