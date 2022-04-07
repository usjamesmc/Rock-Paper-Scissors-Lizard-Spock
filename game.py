from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = Player('Frank')


    def game_mode(self):
        while self.user_input != '1' or self.user_input != '2':
            if self.user_input == '1':
                print('RPSLS Rules')
                print('Rock beats Scissors and Lizard')
                print('Paper beats Rock and Spock')
                print('Scissors beats Paper and Lizard')
                print('Lizard beats Paper Spock')
                print('Spock beats Rock and Scissors')
                self.player_vs_computer()
                
            elif self.user_input == '2':
                print('RPSLS Rules')
                print('Rock beats Scissors and Lizard')
                print('Paper beats Rock and Spock')
                print('Scissors beats Paper and Lizard')
                print('Lizard beats Paper Spock')
                print('Spock beats Rock and Scissors')
                self.player_vs_player()
               
            else:
                print('Not a valid response')    
                self.display_welcome()    
        
    
    def display_welcome(self):
        self.user_input = input('Welcome to Rock Paper Scissors Lizard Spock, please choose between 1 or 2 players: ')
        

    def player_vs_player(self):
        self.player_two = Player('Frank')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.display_game_info()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.chosen_gesture} and {self.player_two.name} chose {self.player_two.chosen_gesture}')
            self.game_phase(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
          

    def game_phase(self, player_one, player_two):
        if player_one == 'Rock' and player_two in ['Paper', 'Spock']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one == 'Paper' and player_two in ['Scissors', 'Lizard']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one == 'Scissors' and player_two in ['Rock', 'Spock']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one == 'Lizard' and player_two in ['Rock', 'Scissors']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one == 'Spock' and player_two in ['Lizard', 'Paper']:
            print(f'{self.player_two.name} wins the round.')
            self.player_two.score += 1
        elif player_one == player_two:
            print('Both players chose the same gesture its a tie')                                        
        else:
            print(f'{self.player_one.name} wins the round.')
            self.player_one.score += 1

    def player_vs_computer(self):
        self.player_two = Computer('Steve Jobs')
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.display_game_info()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.chosen_gesture} and {self.player_two.name} chose {self.player_two.chosen_gesture}')
            self.game_phase(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
    
    def display_game_info(self):
        game_number = 1
        print(f'Round {game_number}')
        print(f'{self.player_one.name}: {self.player_one.score} pts VS {self.player_two.name}: {self.player_two.score} pts.')
        game_number += 1
    
    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')        

        
    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f'{self.player_one.name}, wins the game')
        else:
            print(f'{self.player_two.name}, wins the game')

        

    