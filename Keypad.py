import RPi.GPIO as GPIO
import time

class keypad():

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.matrix={"1817" : "1", "1827":"2", "1822":"3", "2317":"4", "2327":"5", "2322":"6", "2417":"7", "2427":"8", "2422":"9", "2517":"*", "2527":"0", "2522": "#"}
        self.row_pins=[18,23,24,25]
        self.col_pins=[17,27,22]
        for col in self.col_pins:
            GPIO.setup(col, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

        for row in self.row_pins:
            GPIO.setup(row, GPIO.OUT)

    def do_polling(self):
        #Determine currently pressed key
        pressedButton=None
        isPressed=False
        for row in self.row_pins:
            GPIO.output(row,GPIO.HIGH)
            for col in self.col_pins:
                if isPressed==False:
                    if GPIO.input(col)==GPIO.HIGH:
                        pressedButton=self.matrix[str(row)+str(col)]
                        isPressed=True
            GPIO.output(row,GPIO.LOW)
            if isPressed==True:
                break
        return pressedButton
    '''
    def do_polling(self):       #Her er det noe muffins
        is_key_found = False
        key = None
        for row in self.row_pins:
            GPIO.output(row, GPIO.HIGH)
            for col in self.col_pins:
                if is_key_found == False:
                    if GPIO.input(col) == GPIO.HIGH:
                        is_key_found = True
                        key = self.key_dict[str(row)+str(col)]        #Returnerer et tall fra dict
            GPIO.output(row, GPIO.LOW)
            if is_key_found == True:
                break
        return key
        '''


    def get_next_signal(self):
        keys_count=0
        prev_key=None
        key_pressed=None
        while keys_count<100:
            key_pressed=self.do_polling()
            if key_pressed is not None:
                if prev_key is None:
                    prev_key=key_pressed
                    keys_count+=1
                elif prev_key==key_pressed:
                    keys_count+=1
                else:
                    keys_count=0
                    prev_key=None
            time.sleep(0.01)
        return key_pressed


if __name__=="__main__":
    kp=keypad()
    kp.setup()
    button=kp.get_next_signal()
    print(button)