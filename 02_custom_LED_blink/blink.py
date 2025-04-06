from machine import Pin
from utime import sleep
from machine import Timer

pin = Pin("LED", Pin.OUT)

def mycallback(t):
    pin.toggle()

tim = Timer(-1)
tim.init(period=2000, mode=Timer.PERIODIC, callback=mycallback)


print("LED starts flashing...")
while True:
    try:
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
