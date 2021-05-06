from gpiozero import Servo, Button
from time import sleep


servo = Servo(21)
servo.min()

button = Button(20)

#button.wait_for_press()
#print("Button was pressed")

while True:
    #servo.min()
    button.wait_for_press()
    servo.max()
    button.wait_for_press()
    servo.min()

