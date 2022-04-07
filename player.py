class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.score = 0
        self.chosen_gesture = []

    def choose_gesture(self):
        for gesture in self.gesture:
            print(f'{self.gesture.index(gesture)}: {gesture}')

        while True:
            try:
                user_input = int(input('Choose a gesture by number: '))
            except ValueError:
                    print("That is not a valid repsonse.")
                    continue
            else:
                if user_input <= len(self.gesture) - 1:
                    self.current_gesture = self.gesture[int(user_input)]

                else:
                    print("That is not a valid repsonse.")
                self.choose_gesture()
            break    

        

    
    
                                            

