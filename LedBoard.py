import RPi.GPIO as GPIO

class LedBoard():


    def setup(self):
        GPIO.setmode(GPIO.BCM)

    def light_led(self,ledno,duration):
        #Turn on led #ledno for duration

    def flash_all_leds(self,k):
        #Flash leds with intervals of k seconds

    def twinkle_all_leds(self,k):
        #Twinkle leds in k-lasting sequences
