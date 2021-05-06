import pigpio

from time import sleep


pi = pigpio.pi()

pin = 21

while True:
    pi.set_servo_pulsewidth(pin,0)
    sleep(1)
    pi.set_servo_pulsewidth(pin, 1000)
    sleep(1)


