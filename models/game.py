from models.player import *
# from models.players import add_loser, add_winner

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

winners = []
losers = []

def add_winner(player):
    winners.append(player)


def add_loser(player):
    losers.append(player)

def play(player1, player2):
    if player1.choice == "Rock" and player2.choice == "Scissors":
        return f"{player1.name} is the winner"
        add_winner(player)
    if player1.choice == "Scissors" and player2.choice == "Paper":
        return f"{player1.name} is the winner"

    if player1.choice == "Paper" and player2.choice == "Rock":
        return f"{player1.name} is the winner"

    if player1.choice == "Rock" and player2.choice == "Paper":
        return f"{player2.name} is the winner"

    if player1.choice == "Scissors" and player2.choice == "Rock":
        return f"{player2.name} is the winner"

    if player1.choice == "Paper" and player2.choice == "Scissors":
        return f"{player2.name} is the winner"

    return None
