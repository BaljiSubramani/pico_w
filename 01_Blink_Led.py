import machine
import time
led = machine.Pin("LED",machine.Pin.OUT)
while(1):
    led.off()
    time.sleep(0.5)
    led.on()
    time.sleep(0.5)
