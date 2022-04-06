import random
from player import Player
class Computer(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def attack_choice(self):   
        computer_choice = random.choice(self.gesture)
        return computer_choice

    

