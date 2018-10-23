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


