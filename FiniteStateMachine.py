from inspect import isfunction

class FSM():


    def __init__(self,agent,keypad,ledboard):
        self.agent=agent
        self.keypad=keypad
        self.ledboard=ledboard
        self.rules=[]

    def add_rule(self,rule):
        self.rules.append(rule)

    def get_next_signal(self):
        return self.agent.get_signal()

    def run_rules(self):
        #Go through rules and apply or fire rules

    def fire_rule(self):
        #Switch states and call appropriate agent method

    def apply_rule(self):
        #Control if rule-conditions are met

    def main_loop(self):
        def signal_is_digit(signal):return 48 <= ord(signal) <= 57
        rule.symbol=signal_is_digit
        #Loop through and change states until FSM reaches full state
        #Create rules
        currentState=0


