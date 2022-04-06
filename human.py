from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()
        

    def attack_choice(self):   
        user_input = input(f'Please select your weapon of choice.: ')
        print (user_input)