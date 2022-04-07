from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = Player('Frank')
        

    def run_game(self):
        self.display_welcome()
        if self.user_input == '1':
            print('You will be facing a computer')
            self.player_vs_computer()
            
        else:
            print('You will be facing a human')
            self.player_vs_player()
            


        self.display_winner()
        
    
    def display_welcome(self):
        self.user_input = input('Choose between 1 or 2 players: ')
        

    
    def player_vs_player(self):
        self.player_two = Player('Frank')
        while self.player_one.score < 2 and self.player_two.score < 2:
            choice = self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.chosen_gesture} and {self.player_two.name} chose {self.player_two.chosen_gesture}')
            self.game_phase(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
        return choice    
       
    def player_vs_computer(self):
        self.player_two = Computer('Steve Jobs')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.chosen_gesture} and {self.player_two.name} chose {self.player_two.chosen_gesture}')
            self.game_phase(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
    
    def game_phase(self, player_one_choice, player_two_choice):
        if player_one_choice == 'Rock' and player_two_choice in ['Paper', 'Spock']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one_choice == 'Paper' and player_two_choice in ['Scissors', 'Lizard']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one_choice == 'Scissors' and player_two_choice in ['Rock', 'Spock']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one_choice == 'Lizard' and player_two_choice in ['Rock', 'Scissors']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one_choice == 'Spock' and player_two_choice in ['Lizard', 'Paper']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one_choice == player_two_choice:
            print('Both players chose the same gesture its a tie')                                        
        else:
            print(f'{self.player_one} wins the round.')
            self.player_one.score += 1
    
    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')        

        
    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f'{self.player_one.name}, wins the game')
        else:
            print(f'{self.player_two.name}, wins the game')

        

    