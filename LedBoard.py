import RPi.GPIO as GPIO

class LedBoard():


    def __init__(self):
        GPIO.setup(pin,GPIO.IN)
        GPIO.setup(pin,GPIO.OUT)