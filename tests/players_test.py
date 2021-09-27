import unittest
from models.players import *
from models.player import *
from models.game import *


class TestPlayers(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Drew", "Rock")
        self.player2 = Player("Gemma", "Scissors")
        self.player3 = Player("Harley", "Paper")
        self.player4 = Player("Smiggle", "Hello")
        game1 = Game(player1, player2)
        game2 = Game(player2, player3)
        game3 = Game(player3, player1)
        game4 = Game(player4, player1)
