from gpiozero import LED
from time import sleep

red = LED(27)
red.on()
sleep(1)
for i in range(10):
    red.toggle
    sleep(1)
