import json
import logging
import random

log = logging.getLogger("ticket_to_ride")
log.setLevel(logging.DEBUG)


def init():
    with open("init.json") as config:
        initFile = json.load(config)
        log.debug(initFile)
        return initFile


def drawTrainCard(trainCards):
    colors = list(trainCards.keys())
    color = colors[random.randint(0, len(colors) - 1)]
    trainCards[color] = trainCards[color] - 1
    log.debug(color)
    return [color, trainCards]


