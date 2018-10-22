class KPC():


    def __init__(self,keypad,ledBoard):
        self.keypad=keypad
        self.ledBoard=ledBoard
        self.__pass_file="passcode.txt"

    def init_passcode_entry(self):
        #Power up and clear passcode-buffer

    def get_next_signal(self):
        #return override-signal, wait for keypress

    def verify_login(self,loginText):
        return open(self.__pass_file).readline()