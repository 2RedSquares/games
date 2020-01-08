import json
import logging
import random

log = logging.getLogger("ticket_to_ride")
log.setLevel(logging.DEBUG)


class State:
    trainCards = {}


def init():
    with open("init.json") as config:
        x = json.load(config)
        state = State()
        state.trainCards = x["trainCards"]
        return state


def drawCards(draw, deck, num):
    if (num == 0):
        return ()
    else:
        return (draw(deck),) + drawCards(draw, deck, num - 1)


def drawTrainCard(trainCards):
    colors = list(trainCards.keys())
    color = colors[random.randint(0, len(colors) - 1)]
    trainCards[color] = trainCards[color] - 1
    log.debug(color)
    return color
