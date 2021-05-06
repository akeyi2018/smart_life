from gpiozero import LED
from time import sleep

drive1 = LED(20)
drive2 = LED(16)

drive1.off()
drive2.off()

while True:
    sleep(3)
    drive1.on()
    drive2.off()
    sleep(3)
    drive1.off()
    drive2.on()

