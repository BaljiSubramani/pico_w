import network
import socket
import utime
from machine import Pin

led = Pin(20, Pin.OUT)

state = "off"
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
    
def web_page(state):
    html = f"""
        <!DOCTYPE html>
        <html>
        <form action="./on">
        <input type="submit" value="Turn Light on" />
        </form>
        <form action="./off">
        <input type="submit" value="Turn Light off" />
        </form>
        <p>LED state: {state}</p>
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
        
        if request == "/on?":
            led.value(1)
            state = "ON"
            
        elif request == "/off?":
            led.value(0)
            state = "OFF"
        
        html = web_page(state)
        client.send('HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()
    
except OSError as e:
    print("Error: Connection terminated.")
    client.close()



