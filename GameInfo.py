
# Multiple Inheritance 

class Game():
    def Playing(self):
        print("\t\t\t\t\t\tMini Cazino")
class Rps(Game):
    def Rpsinfo(self):
        print("\n\tRock, Paper, Scissors. The familiar game of Rock, Paper, Scissors is played like this: at the same time, two players(one user, one computer) display one of three symbols: a rock, paper, or scissors. A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.")
class Gtn(Game):
    def Gtninfo(self):
        print("\n\tGuess the Number. Lets you pick a number between 0 to 36. Play the game to achieve true randomness and add the luck factor.")

class Cf(Game):
    def Cfinfo(self):
        print("\n\tCoin flipping, coin tossing, or heads or tails is the practice of throwing a coin in the air and checking which side is showing when it lands, in order to choose between two alternatives, heads or tails, sometimes used to resolve a dispute between two parties.")
        
r = Rps()
r.Playing()
r.Rpsinfo()
g = Gtn()
g.Playing()
g.Gtninfo()
c = Cf()
c.Playing()
c.Cfinfo()
