class Gestures():
    def __init__(self, name):
        self.name = name
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        

    def choose_gesture(self):
        user_input = input(f'Choose your {self.gesture}: ')
        print(f' {self.name} has chosen {user_input} to use.')
        