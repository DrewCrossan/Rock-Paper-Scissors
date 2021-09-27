import unittest
from models.player import *


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Drew", "Rock")
        self.player2 = Player("Gemma", "Scissors")
        self.player3 = Player("Harley", "Paper")
        self.player4 = Player("Smiggle", "Hello")

    def test_player_name(self):
        self.assertEqual("Drew", self.player1.name)
        self.assertEqual("Gemma", self.player2.name)

    def test_player_choice(self):
        self.assertEqual("Rock", self.player1.choice)
        self.assertEqual("Scissors", self.player2.choice)