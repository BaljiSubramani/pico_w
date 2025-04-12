import network
import urequests
import utime

ssid = "Home_103"
password = "Krish101114"

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    
    while wlan.isconnected() == False:
        print("Connecting, Please wait...")
        utime.sleep(1)
        
    print("Connected! IP= ",wlan.ifconfig()[0])
    
try:
    connect()
    site = "https://icanhazdadjoke.com/slack"
    r = urequests.get(site)
    print("query: ",site)
    print(r.json())
    r.close()
    
except OSError as e:
    print("Error: Connection closed")
    r.close()

