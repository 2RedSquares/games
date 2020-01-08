import unittest
from ticket_to_ride import init, drawCards, drawTrainCard


colors = [
            "pink", "white", "black", "green", "red", "orange", "blue",
            "yellow", "locomotive"
        ]


class TestTicketToRide(unittest.TestCase):

    def test_init(self):
        state = init()
        self.assertIsNotNone(state.trainCards)

    def test_drawATrainCard(self):
        state = init()
        color = drawTrainCard(state.trainCards)
        self.assertIn(color, colors)

    def test_drawTwoTrainCards(self):
        state = init()
        hand = drawCards(drawTrainCard, state.trainCards, 2)
        self.assertEqual(len(hand), 2)
        map(lambda x: self.assertIn(x, colors), hand)

    def test_drawFourTrainCards(self):
        state = init()
        hand = drawCards(drawTrainCard, state.trainCards, 4)
        self.assertEqual(len(hand), 4)
        map(lambda x: self.assertIn(x, colors), hand)


if __name__ == '__main__':
    unittest.main()
