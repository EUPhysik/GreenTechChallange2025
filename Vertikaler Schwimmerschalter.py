import time # um einen zyklus des des erfassens festgelegt werden kann.
from gpiozero import Button

sensor = Button(17, pull_up=True)

while True:
    print(sensor.value)
  
    time.sleep(0.5)