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
        return open(self.__pass_file).readline()==loginText

    def validate_passcode_change(self):
        #Control passcode change, 4 digits long, numbers only, change passcode file

    def light_one_led(self):
        #Call ledBoard to light led #Lid for Ldur milliseconds

    def flash_leds(self):
        #Call ledboard to flash all leds

    def twinke_leds(self):
        #I think you understand what this does by now

    def exit_action(self):
        #Call LED power-down-sequence