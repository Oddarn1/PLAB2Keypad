import LedBoard
import Keypad

class KPC():


    def __init__(self,keypad,ledBoard):
        self.keypad=keypad
        self.ledBoard=ledBoard
        self.__pass_file="passcode.txt"
        self.buffer = []
        self.override = ''
        self.lid=0
        self.ldur=0

    def init_passcode_entry(self):
        self.buffer = []
        self.led_power_up()

    def get_next_signal(self):
        return self.override if len(self.override) > 0 else self.keypad.get_next_signal()

    def verify_login(self,loginText):
        if(open(self.__pass_file).readline()==loginText):
            self.override = 'Y'
            self.led_success()
        else:
            self.override = 'N'
            self.led_failure()


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
        open(self.__pass_file, 'w').write(password)

    def light_one_led(self):
        self.ledBoard.light_led(self.lid, self.ldur)

    def flash_leds(self):
        self.ledBoard.flash_all_leds(2)

    def twinke_leds(self):
        self.ledBoard.twinkle_all_leds(2)

    def exit_action(self):
        self.ledBoard.light_led(0, 0.2)
        self.ledBoard.light_led(1, 0.2)
        self.ledBoard.light_led(2, 0.2)
        self.ledBoard.twinkle_all_leds(0.2)

    def led_power_up(self):
        self.ledBoard.twinkle_all_leds(0.2)
        self.ledBoard.light_led(3, 0.2)
        self.ledBoard.light_led(4, 0.2)
        self.ledBoard.light_led(5, 0.2)

    def led_success(self):
        self.twinke_leds()

    def led_failure(self):
        self.flash_leds()

    def new_password(self):
        pass

    def reset_agent(self):
        pass

    def set_lid(self):
        pass

    def logout(self):
        pass

    def set_ldur(self):
        pass

