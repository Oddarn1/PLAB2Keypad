from Keypad import Keypad
from LedBoard import LedBoard

class KPC():


    def __init__(self,keypad,ledBoard):
        self.keypad=keypad
        self.ledBoard=ledBoard
        self.__pass_file="passcode.txt"
        self.buffer = []
        self.override = ''
        self.current_key=None
        self.tmpPassChange=""
        self.lid=0
        self.ldur=0

    def init_passcode_entry(self):
        self.buffer = []
        self.led_power_up()

    def get_next_signal(self):
        if len(self.override) > 0:
            tmp = self.override
            self.override = ''
            self.current_key=tmp
            return tmp
        else:
            tmp=self.keypad.get_next_signal()
            self.current_key = tmp
            return tmp

    def verify_login(self):
        password=""
        for char in self.buffer:
            password+=char
        print(password)
        self.buffer=[]
        with open(self.__pass_file) as f:
            actualpw=f.readline()
        if(int(actualpw)==int(password)):
            self.override = 'Y'
            self.led_success()
        else:
            self.override = 'N'
            self.led_failure()
        self.current_key=None


    def validate_passcode_change(self):
        password = ""
        if len(self.buffer) > 3:
            for elem in self.buffer:
                if not str(elem).isdigit():
                    self.led_failure()
                    return
                password += str(elem)
        else:
            self.led_failure()
            return

        self.led_success()
        if password==self.tmpPassChange:
            f = open(self.__pass_file, 'w')
            f.write(password)
            f.close()
            self.buffer=[]
            self.tmpPassChange=""
        else:
            self.led_failure()
            return

    def store_password_change(self):
        if len(self.buffer)>3:
            for char in self.buffer:
                self.tmpPassChange+=char
        else:
            self.led_failure()
        self.buffer=[]

    def reset(self):
        self.buffer = []
        self.ldur = 0
        self.lid = 0
        self.tmpPassChange=''

    def light_one_led(self):
        self.set_lid()
        self.set_ldur()
        self.ledBoard.light_led(self.lid, self.ldur)
        self.ldur = 0
        self.buffer=[]

    def flash_leds(self):
        self.ledBoard.flash_all_leds(2)

    def twinke_leds(self):
        self.ledBoard.twinkle_all_leds(2)

    def exit_action(self):
        self.ledBoard.light_led(0, 0.2)
        self.ledBoard.light_led(1, 0.2)
        self.ledBoard.light_led(2, 0.2)
        self.ledBoard.twinkle_all_leds(1)

    def led_power_up(self):
        self.ledBoard.twinkle_all_leds(1)
        self.ledBoard.light_led(3, 0.2)
        self.ledBoard.light_led(4, 0.2)
        self.ledBoard.light_led(5, 0.2)

    def led_success(self):
        self.twinke_leds()

    def led_failure(self):
        self.flash_leds()

    def set_lid(self):
        self.lid = int(self.buffer[0])

    def set_ldur(self):
        self.ldur = int(self.buffer[1])

    def append_next_password_digit(self):
        self.buffer.append(self.current_key)
