import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from HandOfCards import *
from PlayingCard import *

class TestHandOfCards(unittest.TestCase):
    def test_init(self):
        # Test at init fungerer (Den bryr seg ikke om du har feil kort eller feil klasse som her)
        hand = HandOfCards(["H3", "S11", "D5", "5"])
        self.assertEqual(type(hand), HandOfCards)

        # Slik den skal brukes...
        hand = HandOfCards([PlayingCard("D", 4), PlayingCard("C", 13)])
        self.assertEqual(type(hand), HandOfCards)

    def test_is_flush(self):
        card1 = PlayingCard("H", 3)
        card2 = PlayingCard("H", 4)
        card3 = PlayingCard("H", 8)
        card4 = PlayingCard("H", 9)
        card5 = PlayingCard("H", 11)
        card6 = PlayingCard("S", 13)
        card7 = PlayingCard("H", 1)

        # For få kort skal returnere False
        hand1 = HandOfCards([card1, card2, card3, card4]) # For få kort
        self.assertEqual(hand1.is_flush(), False)

        # Flush gir True
        hand2 = HandOfCards([card1, card2, card3, card4, card5]) # Vanlig flush
        self.assertEqual(hand2.is_flush(), True)

        # En hand uten flush skal gi False
        hand3 = HandOfCards([card1, card2, card3, card4, card6]) # Uten flush
        self.assertEqual(hand3.is_flush(), False)

        # Hånd med 6 kort skal også gi True
        hand4 = HandOfCards([card1, card2, card3, card4, card5, card7]) # Flush med 6
        self.assertEqual(hand4.is_flush(),True)
    
    def test_str(self):
        # Sjekker om gyldig kort blir str
        hand = HandOfCards([PlayingCard("D", 4), PlayingCard("C", 13)])
        self.assertEqual(type(hand.__str__()), str)
        

if __name__ == "__main__":
    unittest.main()

