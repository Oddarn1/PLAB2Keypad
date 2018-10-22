import RPi.GPIO as GPIO

class keypad():

    def setup(self):
        GPIO.setmode(GPIO.BCM)

    def do_polling(self):
        #Determine currently pressed key

    def get_next_signal(self):
        #Repeated calls to do_polling until something happens