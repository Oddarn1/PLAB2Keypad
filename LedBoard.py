import RPi.GPIO as GPIO
import time


class LedBoard():

    def setup(self):                                        # awesome mother fucking setup!!!
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
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
                self.turn_off_leds()                         # men det feilsøker vi oss frem til
                break


        #Turn on led #pin_index for duration

    def flash_all_leds(self,k):
        t = time.time() + k  # setter grensen på k sek
        current_pin = 0
        while True:
            if time.time() > t:  # stopper loopen etter k sek har gått
                for led_numbers in range(len(self.pins)):
                    self.turn_off_leds()
                break

            self.light_led(current_pin, 0.01)  # kjører light_led() med 0.5 s duration
            current_pin += 1

            if current_pin == 6:
                current_pin = 0
                time.sleep(0.47)
            time.sleep(0.03)
            # Flash leds with intervals of k seconds

    def turn_off_leds(self):
        for i in range(3):
            self.set_pin(i, -1)



    def twinkle_all_leds(self,k):
        t = time.time() + k                                 # setter grensen på k sek
        current_pin = 0
        while True:
            if time.time() > t:                             # stopper loopen etter k sek har gått
                for led_numbers in range(len(self.pins)):
                    self.turn_off_leds()
                break

            self.light_led(current_pin, 0.5)                # kjører light_led() med 0.5 s duration
            current_pin += 1

            if current_pin == 6: current_pin = 0            # resetter current_pin


        #Twinkle leds in k-lasting sequences

