import RPi.GPIO as GPIO
import time

class keypad():

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.matrix=[['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['#','0','*']]
        self.row_pins=[18,23,24,25]
        self.col_pins=[17,27,22]
        for j in range(3):
            GPIO.setup(self.col_pins[j], GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
            GPIO.output(self.col_pins[j], 1)

        for i in range(4):
            GPIO.setup(self.row_pins[i], GPIO.OUT)

    def do_polling(self):
        #Determine currently pressed key

    def get_next_signal(self):
        #Repeated calls to do_polling until something happens