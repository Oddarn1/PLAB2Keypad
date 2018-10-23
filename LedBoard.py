import RPi.GPIO as GPIO
import time


class LedBoard():

    def setup(self):                                        # awesome mother fucking setup!!!
        GPIO.setmode(GPIO.BCM)
        self.pins = [16, 20, 21]
        self.pin_led_states = [[1, 0, -1],  # A
                                [0, 1, -1],  # B
                                [-1, 1, 0],  # C
                                [-1, 0, 1],  # D
                                [1, -1, 0],  # E
                                [0, -1, 1]]  # F

    def set_pin(self, pin_index, pin_state):                # copypaste fra nettside, www.pornhub.com
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)


    def light_led(self, led_number, duration):
        t = time.time() + duration
        while True:                                         # copypaste fra nettiden, krysser fingra
            for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
                self.set_pin(pin_index, pin_state)

            if time.time() > t:                             # vet egt ikke hvordan man skrur av lysene...
                self.set_pin(led_number, -1)                # men det feilsøker vi oss frem til
                break


        #Turn on led #pin_index for duration

    def flash_all_leds(self,k):
        t = time.time() + k
        while True:
            if time.time() % 2 == 0:                        # flasher på alle partall... tror jeg
                for led_number in self.pins:
                    for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
                        self.set_pin(pin_index, pin_state)

            elif time.time() % 2 == 1:                      # skrur av lysene på oddetall
                for led_number in self.pins:
                    self.set_pin(led_number, -1)

            if time.time() > t:                             # stopper etter t sek har gått
                for led_number in self.pins:
                    self.set_pin(led_number, -1)
                break

        #Flash leds with intervals of k seconds

    def twinkle_all_leds(self,k):
        t = time.time() + k                                 # setter grensen på k sek
        current_pin = 0
        while True:
            if time.time() > t:                             # stopper loopen etter k sek har gått
                for led_numbers in self.pins:
                    self.set_pin(led_numbers, -1)
                break

            self.light_led(current_pin, 0.5)                # kjører light_led() med 0.5 s duration
            current_pin += 1

            if current_pin == 6: current_pin = 0            # resetter current_pin


        #Twinkle leds in k-lasting sequences


if __name__=="__main__":
    led=LedBoard()
    led.setup()
    led.light_led(3,10)



'''
    HER ER DETTE JEG COPYPASTA FRA NETTSIDE!
    http://book.pythontips.com/en/latest/enumerate.html

    import RPi.GPIO as GPIO

pins = [18, 23, 24]

pin_led_states = [
  [1, 0, -1], # A
  [0, 1, -1], # B
  [-1, 1, 0], # C
  [-1, 0, 1], # D
  [1, -1, 0], # E
  [0, -1, 1]  # F
]

GPIO.setmode(GPIO.BCM)

def set_pin(pin_index, pin_state):
    if pin_state == -1:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)

def light_led(led_number):
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)

set_pin(0, -1)
set_pin(1, -1)
set_pin(2, -1)

while True:
    x = int(raw_input("Pin (0 to 5):"))
    light_led(x)

'''