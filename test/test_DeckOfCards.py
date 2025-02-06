import unittest
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from DeckOfCards import DeckOfCards


class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_deal_hand(self):
        self.assertEqual(type(self.deck.deal_hand(5)), )

if __name__ == "__main__":
    unittest.main()
