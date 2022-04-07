# This project was written by three contributors, Gerald Miller, Michael Nevius, Nicholas Wolf.
class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.score = 0
        self.chosen_gesture = None

    def choose_gesture(self):
        self.chosen_gesture = self.player_choice(self.gesture, 'gesture')
        if self.chosen_gesture <= len(self.gesture) - 1:
            self.chosen_gesture = self.gesture[int(self.chosen_gesture)]
        else:
         print('That is not a valid repsonse.')
         self.choose_gesture()


    def player_choice(self, list, category):
      for item in list:
         print(f'{list.index(item)}: {item}')
      while True:
         try:
            chosen_gesture = int(input(f'{self.name}, enter a number to choose your {category} : '))
            break
         except ValueError:
            print('That is not a valid repsonse.')
            continue
      return chosen_gesture    

        

    
    
                                            

