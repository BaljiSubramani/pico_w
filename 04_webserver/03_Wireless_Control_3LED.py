import network
import socket
import utime
from machine import Pin

g_led = Pin(20,Pin.OUT)
y_led = Pin(19,Pin.OUT)
r_led = Pin(18,Pin.OUT)

green_state = "OFF"
yellow_state = "OFF"
red_state = "OFF"
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
    
def web_page(green_state,yellow_state,red_state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <form action="./green_on">
        <input type="submit" value="Turn Green Light on" />
        </form>
        <form action="./green_off">
        <input type="submit" value="Turn Green Light off" />
        </form>
        <p>LED green state: {green_state}</p>
        <form action="./yellow_on">
        <input type="submit" value="Turn Yellow Light on" />
        </form>
        <form action="./yellow_off">
        <input type="submit" value="Turn Yellow Light off" />
        </form>
        <p>LED yellow state: {yellow_state}</p>
        <form action="./red_on">
        <input type="submit" value="Turn Red Light on" />
        </form>
        <form action="./red_off">
        <input type="submit" value="Turn Red Light off" />
        </form>
        <p>LED red state: {red_state}</p>
        </body>
        </html>
        """
    return(html)
    
def open_socket():
    address = socket.getaddrinfo("0.0.0.0",80)[0][-1]
    s = socket.socket()
    s.bind(address)
    s.listen(3)
    
    return(s)

connect()

s = open_socket()

try:
    while True:
        client = s.accept()[0]
        request = client.recv(1024)
        request = str(request)
        
        try:
            request = request.split()[1]
        except Indexerror:
            pass
        print(request)
        
        if request == "/green_on?":
            g_led.on()
            green_state = "ON"
            
        elif request == "/green_off?":
            g_led.off()
            green_state = "OFF"
                    
        elif request == "/yellow_on?":
            y_led.on()
            yellow_state = "ON"
            
        elif request == "/yellow_off?":
            y_led.off()
            yellow_state = "OFF"
            
        elif request == "/red_on?":
            r_led.on()
            red_state = "ON"
            
        elif request == "/red_off?":
            r_led.off()
            red_state = "OFF"
        
        html = web_page(green_state,yellow_state,red_state)
        client.send('HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()
    
except OSError as e:
    print("Error: Connection terminated.")
    client.close()



