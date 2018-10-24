from inspect import isfunction
from LedBoard import LedBoard
from Keypad import keypad
from KPC import KPC

class FSM():


    def __init__(self):
        self.rules=[]

    def add_rule(self,rule):
        self.rules.append(rule)

    def create_all_rules(self):
        def signal_is_digit(signal):return 48<=ord(signal)<=57
        def signal_is_asterisk(signal):return signal=='*'


    def get_next_signal(self):
        return self.agent.get_signal()

    def run_rules(self):
        #Go through rules and apply or fire rules

    def fire_rule(self):
        #Switch states and call appropriate agent method

    def apply_rule(self,rule):
        #Control if rule-conditions are met

    def main_loop(self):
        #Loop through and change states until FSM reaches full state
        #Create rules
        self.keypad=keypad()
        self.ledboard=LedBoard()
        self.keypad.setup()
        self.ledboard.setup()
        self.agent=KPC(self.keypad,self.ledboard)
        currentState=0

    def make_rules(self):
        all_symbols = []
        not_hashtag = []
        all_numbers = []
        all_leds = []


        self.add_rule(Rule("S-Init", "S-Read", all_symbols, self.agent.init))
        self.add_rule(Rule("S-Read", "S-Read", all_numbers, self.agent.get_next_signal()))
        self.add_rule(Rule("S-Read", "S-Verify", not_hashtag, self.agent.verify_login(lgihruilghwr78o)))
        self.add_rule(Rule("S-Read", "S-init", all_symbols, SEND TILBAKE TIL INITSTATE))
        '''
        self.add_rule(Rule("S-Verify", "S-Active", Y???, FULLY ACTIVATE AGENT))
        self.add_rule(Rule("S-Verify", "S-init", all_symbols, RESET AGENT))
        '''


class Rule:
    def __init__(self, current_state, next_state, signal, action):
        # self.current_state = current_state                            # Trenger egt ikke denne
        self.next_state = next_state
        self.signal = signal
        self.action = action

