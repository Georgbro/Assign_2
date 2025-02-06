import unittest
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

class TestPlayingCards(unittest.TestCase):
    def test_init(self):
        self.card = self.__init__("H", 5)
        self.assertEqual(type(self.card), type([]))

if __name__ == "__main__":
    unittest.main()
