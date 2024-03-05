import random

class rockPaperScissors:
    #0 player
    #1 computer
    #2 tie
    state = [8,7,5]
    prediction = [.46,.26,.26]
    
    

    def checkWinner(self,player, com):
        result = {('r','r'): 2, ('r','p'): 1, ('r','s'): 0, ('p','r'): 0, ('p','p'): 2, ('p','s'): 1, ('s','r'): 1, ('s','p'): 0, ('s','s'): 2}

        return result[(player,com)]
    
    def normalisation(self):
        normal = 0
        if sum(self.state) == 0:
            return 1
        
        for i,p in enumerate(self.prediction):
            normal+=(self.state[i]/sum(self.state))*self.prediction[i]
        return normal
    
    def predict(self):
        normal = self.normalisation()
        previousState = self.state[:]
        
        newPrediction = []
        for i,p in enumerate(self.prediction):
            n = sum(previousState)
            if n == 0:
                n = 1
            pred = ((previousState[i]/n)*p)/normal
            newPrediction.append(pred)
            
        print("Probality of next win, player",newPrediction[0],"computer", newPrediction[1], "tie", newPrediction[2])
            
        return newPrediction
    
    def play(self):
        play = True
        plays = ['r','s','p']
        self.predict()
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
            
            
            print(self.state)
            play = input("Do you want to continue? y/n ")
            if play == 'y':
                play = True
            else:
                play = False
                


game = rockPaperScissors()
game.play()