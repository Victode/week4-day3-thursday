import unittest
from hw import Deck, Hand, Game

class TestCart(unittest.TestCase):

    def test_shuffle(self):
        test_shuffle = Deck()

        test_shuffle.shuffle()

    def test_deal(self):
        test_deal = Deck()

        test_deal.deal()

    def test_hitOrStand(self):
        test_stand = Game()

        test_stand.hit_or_stand('s')
        
    
    def test_deck(self):
        test_deckAmount = Deck()

        test_deckAmount.__init__()
        self.assertTrue(test_deckAmount.deck)


if __name__ == '__main__':
    unittest.main()