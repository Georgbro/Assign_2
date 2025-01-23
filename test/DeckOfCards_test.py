import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))


from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards
test_deck = DeckOfCards()

def test_init(DeckOfCards):
    test_deck.__init__()
    print(test_deck)

def test_deal_hand(DeckOfCards):
    hand = test_deck.deal_hand(6)
    print(hand)
    

test_init(DeckOfCards)
test_deal_hand(DeckOfCards)