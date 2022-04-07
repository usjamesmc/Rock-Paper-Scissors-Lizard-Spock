class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.score = 0
        self.chosen_gesture = None

    def choose_gesture(self):
        for gesture in self.gesture:
            print(f'{self.gesture.index(gesture)}: {gesture}')

        while True:
            try:
                self.chosen_gesture = int(input('Choose a gesture by number :'))
                self.current_gesture = self.gesture[int(self.chosen_gesture)]
            except ValueError:
                    print("That is not a valid repsonse.")
                    continue
            else:
                if self.chosen_gesture <= len(self.gesture) - 1:
                    self.current_gesture = self.gesture[int(self.chosen_gesture)]

                else:
                    print("That is not a valid repsonse.")
                self.choose_gesture()
            break    

        

    
    
                                            

