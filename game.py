# This project was written by three contributors, Gerald Miller, Michael Nevius, Nicholas Wolf.
from player import Player
from computer import Computer


class Game:
    def __init__(self):
        self.player_one = Player('Bob')
        self.player_two = Player('Frank')
        self.game_number = 1

    def run_game(self):
        self.display_welcome()
        self.game_mode()
        self.game_phase()
        self.display_winner()
        self.end_game()

    def display_welcome(self):
        self.user_input = input('Welcome to Rock Paper Scissors Lizard Spock, please choose between 1 or 2 players: ')

    def game_mode(self):
        while self.user_input != '1' or self.user_input != '2':
            if self.user_input == '1':
                print('RPSLS Rules')
                print('Rock beats Scissors and Lizard')
                print('Paper beats Rock and Spock')
                print('Scissors beats Paper and Lizard')
                print('Lizard beats Paper Spock')
                print('Spock beats Rock and Scissors')
                self.player_two = Computer('Steve Jobs')
                self.player_selection()
                
            elif self.user_input == '2':
                print('RPSLS Rules')
                print('Rock beats Scissors and Lizard')
                print('Paper beats Rock and Spock')
                print('Scissors beats Paper and Lizard')
                print('Lizard beats Paper Spock')
                print('Spock beats Rock and Scissors')
                self.player_two = Player("Frank")
                self.player_selection()
         
            else:
                print('Not a valid response')    
                self.display_welcome()    
          
          

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

    def display_score(self): 
        print(f'{self.player_one.name} has {self.player_one.score} points and {self.player_two.name} has {self.player_two.score} points.')

    def player_selection(self):
        if self.player_one.score < 2 or self.player_two.score < 2:
            if self.player_one.score == 2:
                self.display_winner()
                self.end_game()
                
            elif self.player_two.score == 2:
                self.display_winner()
                self.end_game()
            
            self.display_game_info()
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            print(f'{self.player_one.name} chose {self.player_one.chosen_gesture} and {self.player_two.name} chose {self.player_two.chosen_gesture}')
            self.game_phase(self.player_one.chosen_gesture, self.player_two.chosen_gesture)
            self.player_selection()

                     
    
    def display_game_info(self):
        print(f'Round {self.game_number}')
        print(f'{self.player_one.name}: {self.player_one.score} pts VS {self.player_two.name}: {self.player_two.score} pts.')
        self.game_number += 1
    
          
        
    def display_winner(self):
        if self.player_one.score == 2:
            print(f'{self.player_one.name}, wins the game')
        else:
            print(f'{self.player_two.name}, wins the game')
    
        
    def end_game(self):
        print('Thanks for playing')
        exit()

        

    