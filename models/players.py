from models.player import *
from models.game import *

player1 = Player("Drew", "Rock")
player2 = Player("Gemma", "Scissors")
player3 = Player("Harley", "Paper")
player4 = Player("Smiggle", "Hello")

players = [player1, player2, player3, player4]
winners = []
losers = []

game1 = Game(player1, player2)
game2 = Game(player2, player3)
game3 = Game(player3, player1)
game4 = Game(player4, player1)

# def add_winner(player):
#     winners.append(player)


# def add_loser(player):
#     losers.append(player)