from machine import UART, Pin
import time

# Initialize UART0 (TX=GPIO0, RX=GPIO1)
uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
Led = Pin("LED", Pin.OUT)  # Initialize LED pin

# Loop to send debug messages
counter = 0
while True:
    message = f"Debug count: {counter}\n"
    uart0.write(message)
    counter += 1
    Led.toggle()  # Toggle LED state
    time.sleep(1)
