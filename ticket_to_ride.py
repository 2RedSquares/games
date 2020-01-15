import functools
import json
import logging
import random

log = logging.getLogger("ticket_to_ride")
log.setLevel(logging.DEBUG)


def compose(*functions):
    def compose2(f, g):
        return lambda x: f(g(x))
    return functools.reduce(compose2, functions, lambda x: x)


def configFactory():
    init = open("init.json")
    config = json.load(init)
    init.close()

    def get():
        return config

    return get


def deckFactory(deck, draw):
    log.debug(deck)

    def drawCards(num):
        if (num == 0):
            return ()
        else:
            return (draw(deck),) + drawCards(num - 1)

    return drawCards


def drawTrainCard(deck):
    colors = list(deck.keys())
    color = colors[random.randint(0, len(colors) - 1)]
    deck[color] = deck[color] - 1
    log.debug(color)
    return color
