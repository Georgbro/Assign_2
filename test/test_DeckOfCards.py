import unittest
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from DeckOfCards import *


class TestDeckOfCards(unittest.TestCase):
    def test_init(self):
        deck = DeckOfCards()
        self.assertEqual(type(deck), DeckOfCards)

    def test_deal_hand(self):
        deck = DeckOfCards()

        # Tester at rett HandOfCards blir opprettet
        self.assertEqual(type(deck.deal_hand(4)), HandOfCards)

        # Tester at feil blir hevet dersom for mange eller for få kort blir delt
        with self.assertRaises(ValueError):
            deck.deal_hand(53)
        with self.assertRaises(ValueError):
            deck.deal_hand(0)

    def test_str(self):
        deck = DeckOfCards()

        self.assertEqual(type(deck.__str__()), str)
        


if __name__ == "__main__":
    unittest.main()
