import random

class rockPaperScissors:
    #0 player
    #1 computer
    #2 tie
    state = [7,4,1]
    prediction = [.33,.33,.33]
    
    

    def checkWinner(self,player, com):
        result = {('r','r'): 2, ('r','p'): 1, ('r','s'): 0, ('p','r'): 0, ('p','p'): 2, ('p','s'): 1, ('s','r'): 1, ('s','p'): 0, ('s','s'): 2}

        return result[(player,com)]
    
    def normalisation(self):
        norm = 0
        for i, p in enumerate(self.prediction):
            norm += self.getProbabilityOfPlayer(i)*p
        return norm

    def getProbabilityOfPlayer(self,i):
        return self.state[i]/sum(self.state)

    
    def predict(self):
        newPrediction = []
        for i, p in enumerate(self.prediction):
            probability = self.getProbabilityOfPlayer(i)
            newPrediction.append((probability * p)/self.normalisation())
        self.prediction = newPrediction
        return self.prediction
    
    def play(self):
        play = True
        plays = ['r','s','p']
        
        while(play) :
            player = input('Enter your choice (r for rock, p for paper, s for scissors: ')

            com = random.choice(plays)
            
            print("Computer choice: ", com)

            winner = self.checkWinner(player, com)
            
            if winner == 0:
                print("Player wins")
            elif winner == 1:
                print("Computer wins")
            else:
                print("It is a tie")
            
            
            self.state[winner] +=1
            
            self.prediction = self.predict()
            
            print("Current state",self.state)
            print("Predictions:",self.prediction)

            play = input("Do you want to continue? y/n ")
            if play == 'y':
                play = True
            else:
                play = False
                


game = rockPaperScissors()
game.play()