import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace = Card('hearts',1)
        self.card2 = Card('hearts', 5)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertTrue(self.card_game(self.ace))
        