from player import Player
from computer import Computer
class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = Computer('Frank')
        self.player_one_score = 0
        self.player_two_score = 0

    def run_game(self):
        self.display_welcome()
        self.game_phase()
        self.display_winner()
    def display_welcome(self):
        print('Welcome to Rock Paper Scissors Lizard Spock')
        user_input = input('Choose between 1 or 2 players: ')
        if user_input == '1':
            print('You will be facing a computer')
        else:
            print('You will be facing a human')
    def game_phase(self):
        user_input = input(f'Enter a choice from{self.gesture}')
        if user_input == self.player_two:
            print(f"Both players selected {self.gesture}. It's a tie!")
        elif user_input == 'Rock':
            if self.player_two == 'Scissors':
                print('Rock smashes scissors')
            else:
                print('Paper covers rock') 
            self.player_one_score =+1    
        
    def display_winner(self):
        if self.player_one_score == 2:
            print(f'{self.player_one.name}, wins the game')
        else:
            print(f'{self.player_two.name}, wins the game')

    