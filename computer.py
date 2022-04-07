import random
from player import Player
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)

    def attack_choice(self):   
        self.chosen_gesture = random.choice(self.gesture)
        

    

