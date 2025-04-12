from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import utime

def pin_cleanup():
    for i in range(0,29):
        try:
            Pin(i,Pin.OUT,value=0)
            utime.sleep_ms(10)
        except:
            print("Exception")

pin_cleanup()

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(17), sda=Pin(16))

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

oled.poweroff()
utime.sleep(1)

oled.poweron()
utime.sleep(1)

while True: 
  
    oled.text('Hello, I am ', 0, 0)
    oled.show()
    utime.sleep(1)
    
    oled.text('Krishnan!   ', 0, 10)
    oled.show()
    utime.sleep(1)
    
    oled.text('How are you!', 0, 20)
    oled.show()
    utime.sleep(1)
    
    oled.text('Naruto Uzimaki', 0, 30)
    oled.show()
    utime.sleep(1)
    
    oled.fill(0)
    oled.show()
    utime.sleep(1)

