from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = None


    def run_game(self):
        self.display_welcome()
        self.game_phase()
        self.display_winner()
        self.display_score()
    
    def display_welcome(self):
        user_input = input('Choose between 1 or 2 players: ')
        print('Welcome to Rock Paper Scissors Lizard Spock') 
        if user_input == '1':
            print('You will be facing a computer')
        else:
            print('You will be facing a human')

    
    def player_vs_player(self):
        self.player_two = Player('Frank')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.choose_winner(self.player_one.current_gesture, self.player_two.current_gesture)
            self.display_score()
       
    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')


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

        

    