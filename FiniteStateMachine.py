from inspect import isfunction
import re
import inspect
from LedBoard import LedBoard
from Keypad import Keypad
from KPC import KPC


class FSM:

    def __init__(self, agent):
        self.rules = []
        self.current_state = "S_init"
        self.agent = agent

    def add_rule(self,rule):
        # add a new rule to the end of the FSM's rule list
        self.rules.append(rule)

    def get_next_signal(self):
        # query the agent for the next signal
        return self.agent.get_next_signal()

    def run_rules(self, signal):
        # Go through rules and apply or fire rules
        for i in self.rules:
            x = self.apply_rule(i, signal)
            if x:
                break
        return

    def fire_rule(self, rule, signal):
        # use the consequent of a rule to:
        # a) set the next state of the FSM, and
        # b) call the appropriate agent action method
        self.current_state=rule.next_state
        if self.signal_is_digit(signal):
            rule.action(signal)
        else:
            rule.action()

    def matches(self, rule, s):
        if inspect.ismethod(rule.signal):
            x = rule.signal(s)
        else:
            x = (rule.signal == s)
        return x and self.current_state == rule.current_state

    def apply_rule(self, rule, signal):
        # Control if rule-conditions are met
        if self.matches(rule, signal):
            self.fire_rule(rule, signal)
            return True
        else:
            return False


    def make_all_rules(self):           # Need to put in symbols

        init_rule = Rule("S_init", "S_read", "*", self.agent.init_passcode_entry)
        self.add_rule(init_rule)
        read1_rule = Rule("S_read", "S_read", self.signal_is_digit, self.agent.append_next_password_digit)
        self.add_rule(read1_rule)
        read2_rule = Rule("S_read", "S_verify", "*", self.agent.verify_login)
        self.add_rule(read2_rule)
        read3_rule = Rule("S_read", "S_init", "#", self.agent.reset)                  # self.agent.reset_agent ???
        self.add_rule(read3_rule)
        verify_rule = Rule("S_verify", "S_active", "Y", self.agent.twinke_leds)
        self.add_rule(verify_rule)
        verify2_rule = Rule("S_verify", "S_init", "N", self.agent.reset)            # self.agent.reset_agent ???
        self.add_rule(verify2_rule)
        active1_rule = Rule("S_active", "S_read2", "*", self.agent.init_passcode_entry)
        self.add_rule(active1_rule)
        read4_rule= Rule("S_read2","S_read2",self.signal_is_digit,self.agent.append_next_password_digit)
        self.add_rule(read4_rule)
        read5_rule=Rule("S_read2","S_read3","*",self.agent.store_password_change)
        self.add_rule(read5_rule)
        read6_rule=Rule("S_read3","S_read3",self.signal_is_digit,self.agent.append_next_password_digit)
        self.add_rule(read6_rule)
        verify3_rule=Rule("S_read3","S_active","*",self.agent.validate_passcode_change)
        self.add_rule(verify3_rule)
        active2_rule = Rule("S_active", "S_led", self.signal_is_digit, self.agent.set_lid)
        self.add_rule(active2_rule)
        active3_rule = Rule("S_active", "S_logout", "#", self.agent.init_passcode_entry)
        self.add_rule(active3_rule)
        led_rule = Rule("S_led", "S_time", self.signal_is_digit, self.agent.set_ldur)
        self.add_rule(led_rule)
        time_rule = Rule("S_time", "S_time", self.signal_is_digit, self.agent.set_ldur)
        self.add_rule(time_rule)
        light_rule = Rule("S_time", "S_active", "*", self.agent.light_one_led)
        self.add_rule(light_rule)
        logout_rule = Rule("S_logout", "S_done", "#", self.agent.exit_action)
        self.add_rule(logout_rule)

    @staticmethod
    def all_symbols(sym):
        if sym.isdigit() or sym == "#" or sym == "*":
            return True
        else:
            return False

    @staticmethod
    def signal_is_digit(sym):
        return 48 <= ord(sym) <= 57


class Rule:
    def __init__(self,current_state,next_state, signal, action):
        self.next_state = next_state
        self.current_state=current_state
        self.signal = signal
        self.action = action


def main_loop():
    kp=Keypad()
    kp.setup()
    lb=LedBoard()
    lb.setup()
    agent = KPC(kp,lb)
    fsm = FSM(agent)
    fsm.make_all_rules()
    while fsm.current_state != "S_done":
        signal = fsm.get_next_signal()
        print(signal)
        fsm.run_rules(signal)
        print(fsm.current_state)


if __name__ == '__main__':
    main_loop()
