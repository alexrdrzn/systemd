from gpiozero import LED
from time import sleep

red = LED(17)
red.on()
sleep(1)
for i in range(20):
    red.toggle()
    sleep(0.5)
