# This project was written by three contributors, Gerald Miller, Michael Nevius, Nicholas Wolf.
import random
from player import Player
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):   
        self.chosen_gesture = random.choice(self.gesture)
        

    

