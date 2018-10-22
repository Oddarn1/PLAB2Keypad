import RPi.GPIO as GPIO

class keypad():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for rp in GPIO:
            GPIO.setup(rp,GPIO.OUT)