from player import Player

class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = Player('Frank')

    def run_game(self):
        self.display_welcome()
        self.game_phase()
        self.display_winner()
    def display_welcome(self):
        print('Welcome to Rock Paper Scissors Lizard Spock')
    def game_phase(self):
        user_input = input('Choose between 1 or 2 players: ')
        if user_input == '1':
            print('You will be facing a computer')
        else:
            print('You will be facing a human')
        
    def display_winner(self):
        print()

    