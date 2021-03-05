try :
    import usocket as socket
except:
  import socket
from machine import Pin
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
ssid = 'WIFI_A023'
password = 'ADMINA023'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(17, Pin.OUT)

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(1)

while True:
  conn, addr = s.accept()
  print('connection établie avec %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Contenu de la requète = %s' % request,'\n')
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  debut_reponse = 'HTTP/1.1 200 OK\n Content-Type: text/html\n Connection: close\n\n'
  reponse = debut_reponse + web_page()
  print("réponse du serveur : \n",reponse,'\n')
  conn.sendall(reponse)
  conn.close()