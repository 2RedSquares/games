import unittest
from ticket_to_ride import configFactory, deckFactory, drawTrainCard


colors = [
    "pink", "white", "black", "green", "red", "orange", "blue",
    "yellow", "locomotive"
]


def givenTrainDeck():
    getConfig = configFactory()
    drawCards = deckFactory(getConfig()["trainCards"], drawTrainCard)
    return drawCards


def thenCardFromTrainDeck(cards):
    map(lambda card: unittest.assertIn(card, colors), cards)


class TestTicketToRide(unittest.TestCase):

    def test_getConfig(self):
        getConfig = configFactory()
        self.assertIsNotNone(getConfig()["trainCards"])

    def test_drawATrainCard(self):
        draw = givenTrainDeck()
        cards = draw(1)
        thenCardFromTrainDeck(cards)

    def test_drawTwoTrainCards(self):
        draw = givenTrainDeck()
        cards = draw(2)
        thenCardFromTrainDeck(cards)


if __name__ == '__main__':
    unittest.main()
