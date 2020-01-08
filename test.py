import unittest
from ticket_to_ride import init, drawTrainCard


class TestTicketToRide(unittest.TestCase):
    def test_init(self):
        x = init()
        self.assertIsNotNone(x["trainCards"])

    def test_drawTrainCard(self):
        trainCards = init()["trainCards"]
        [color, deck] = drawTrainCard(trainCards)
        self.assertIn(color, [
            "pink", "white", "black", "green", "red", "orange", "blue",
            "yellow", "locomotive"
        ])


if __name__ == '__main__':
    unittest.main()
