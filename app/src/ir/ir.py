from gpiozero import Button

import os 

def irSensor():
    sensePin = 3
    senseButton = Button(sensePin)
    
    status = senseButton.is_pressed
    if status == True:
        print("sensor.detceted")
        return True
    else:
        return False

            