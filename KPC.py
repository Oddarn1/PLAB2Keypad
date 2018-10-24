import LedBoard
import Keypad
import FiniteStateMachine

class KPC():


    def __init__(self,keypad,ledBoard):
        self.keypad=keypad
        self.ledBoard=ledBoard
        self.__pass_file="passcode.txt"
        self.lid=0
        self.ldur=0

    def init_passcode_entry(self):
        #Power up and clear passcode-buffer

    def get_next_signal(self):
        #return override-signal, wait for keypress

    def verify_login(self,loginText):
        with open(self.__pass_file) as f:
            return f.readlines()=="loginText"

    def validate_passcode_change(self):
        # TODO

    def light_one_led(self):
        self.ledBoard.light_led(self.lid, self.ldur)

    def flash_leds(self):
        self.ledBoard.flash_all_leds(2)

    def twinke_leds(self):
        self.ledBoard.twinkle_all_leds(2)

    def exit_action(self):
        #Call LED power-down-sequence