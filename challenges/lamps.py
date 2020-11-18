import threading
import time
import random

class Board():

    def __init__(self, quant, blink_type):
        self.lamps = [Lamp(i, blink_type, quant) for i in range(quant)]
        self.blink_type = blink_type

    def turn_on(self):
        self.state = 1
        for lamp in self.lamps:
            lamp.state = 1
            lamp.proc.start()
        self.lamps[0].event.set()
        self.lamps[0].event.clear()

    def turn_off(self):
        self.state = 0
        for lamp in self.lamps:
            lamp.state = 0
            lamp.proc.join()


class Lamp():

    def __init__(self, id, blink_type, quant):
        self.id = id
        self.state = 0
        self.quant = quant
        self.blink_type = blink_type
        self.event = threading.Event()
        self.proc = threading.Thread(target=self.blink, daemon=True)
        print(f"lamp {self.id} created")


    def blink(self):
        while self.state == 1:
            
            if self.blink_type == "line":
                self.event.wait()
            
            print(f"lamp {self.id} turned on")
            time.sleep(random.randint(3,7))
            print(f"lamp {self.id} turned off")
            time.sleep(random.randint(1,2))
            
            if self.blink_type == "line":
                next_id = self.id + 1 if self.id < self.quant - 1 else 0
                board.lamps[next_id].event.set()
                board.lamps[next_id].event.clear()



if __name__ == "__main__":
    print("random lamps")
    board = Board(3,"rand")
    board.turn_on()
    time.sleep(15)
    board.turn_off()

    print("")

    print("lamps in line")
    board = Board(3,"line")
    board.turn_on()
    time.sleep(15)
    board.turn_off()