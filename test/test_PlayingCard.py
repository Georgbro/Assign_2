import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from PlayingCard import *

class TestPlayingCards(unittest.TestCase):

    def test_init(self):
        # Test at init fungerer
        card = PlayingCard("H", 5)
        self.assertEqual(type(card), PlayingCard)

        # Test ugyldige input for suit
        with self.assertRaises(ValueError):
            PlayingCard("X", 5)  

        # Test ugyldige input for face
        with self.assertRaises(ValueError):
            PlayingCard("H", 0)  # Face er utenfor gyldig intervall
        with self.assertRaises(ValueError):
            PlayingCard("H", 14)  # Face er utenfor gyldig intervall

    def test_get_as_string(self):
        # Test at kortet returnerer riktig streng
        card = PlayingCard("H", 5)
        self.assertEqual(card.get_as_string(), "H5")

        card = PlayingCard("D", 10)
        self.assertEqual(card.get_as_string(), "D10")

    def test_get_suit(self):
        # Test at get_suit returnerer riktig suit
        card = PlayingCard("H", 5)
        self.assertEqual(card.get_suit(), "H")

        card = PlayingCard("D", 10)
        self.assertEqual(card.get_suit(), "D")

    def test_get_face(self):
        # Test at get_face returnerer riktig face value
        card = PlayingCard("H", 5)
        self.assertEqual(card.get_face(), 5)

        card = PlayingCard("C", 12)
        self.assertEqual(card.get_face(), 12)

    def test_eq(self):
        # Test likhet mellom kort
        card1 = PlayingCard("H", 5)
        card2 = PlayingCard("H", 5)
        card3 = PlayingCard("S", 5)
        card4 = PlayingCard("H", 10)

        self.assertEqual(card1, card2) 
        self.assertNotEqual(card1, card3) 
        self.assertNotEqual(card1, card4)  

        # Test at sammenligning med en ikke-PlayingCard returnerer False
        self.assertNotEqual(card1, "H5")

    def test_hash(self):
        # Test at hash-verdien er konsistent for samme kort
        card1 = PlayingCard("H", 5)
        card2 = PlayingCard("H", 5)
        card3 = PlayingCard("D", 5)

        self.assertEqual(hash(card1), hash(card2))  # Samme suit og face
        self.assertNotEqual(hash(card1), hash(card3))  # Ulik suit

if __name__ == "__main__":
    unittest.main()
