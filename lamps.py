import threading
import time
import random

class Board():

    def __init__(self, quant, blink_type):
        self.lamps = [Lamp(i) for i in range(quant)]
        self.blink_type = blink_type

    def turn_on(self):
        if self.blink_type == "rand":
            self.state = 1
            while self.state == 1:
                time.sleep(1)
                for lamp in self.lamps:
                    if lamp.state == 0:
                        x = threading.Thread(target=lamp.blink, args=(id,), daemon=True)
                        x.start()

        elif self.blink_type == "line":
            self.state = 1
            while self.state == 1:
                for lamp in self.lamps:
                    if lamp.state == 0:
                        x = threading.Thread(target=lamp.blink, args=(id,))
                        x.start()
                        x.join()

    def turn_off(self):
        self.state = 0



class Lamp():


    def __init__(self, id):
        self.id = id
        self.state = 0
        print(f"lamp {self.id} created")

    def blink(self, id):
        print(f"lamp {self.id} turned on")
        self.state = 1
        time.sleep(random.randint(5,10))
        print(f"lamp {self.id} turned off")
        self.state = 0








if __name__ == "__main__":
    print("random lamps")
    board = Board(3,"rand")
    proc = threading.Thread(target=board.turn_on)
    proc.start()
    time.sleep(10)
    board.turn_off()
    proc.join()

    print("lamps in line")
    board = Board(3,"line")
    proc = threading.Thread(target=board.turn_on)
    proc.start()
    time.sleep(10)
    board.turn_off()
    proc.join()