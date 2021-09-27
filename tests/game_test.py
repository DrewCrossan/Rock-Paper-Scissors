import unittest
from models.game import *
from models.player import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Drew", "Rock")
        self.player2 = Player("Gemma", "Scissors")
        self.player3 = Player("Harley", "Paper")
        self.player4 = Player("Smiggle", "Hello")

    def test_rock_beats_scissors(self):
        result = play(self.player1, self.player2)

        self.assertEqual(f"{self.player1.name} is the winner", result)

    def test_scissors_beats_paper(self):
        result = play(self.player2, self.player3)

        self.assertEqual(f"{self.player2.name} is the winner", result)

    def test_paper_beats_rock(self):
        result = play(self.player3, self.player1)
        
        self.assertEqual(f"{self.player3.name} is the winner", result)

    def test_rock_loeses_paper(self):
        result = play(self.player1, self.player3)

        self.assertEqual(f"{self.player3.name} is the winner", result)

    def test_scissors_loses_rock(self):
        result = play(self.player2, self.player1)

        self.assertEqual(f"{self.player1.name} is the winner", result)

    def test_paper_loses_scissors(self):
        result= play(self.player3, self.player2)

        self.assertEqual(f"{self.player2.name} is the winner", result)

    def test_return_none(self):
        result = play(self.player1, self.player4)

        self.assertEqual(None, result)

    