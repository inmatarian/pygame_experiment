#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import logging, pygame, random
from logging import debug, info, warning, error, critical
from loadscreen import *
from menuscreen import *
from services import *

class MainGame(object):
    def __init__(self):
        logging.basicConfig( level=logging.DEBUG,
                             format="%(levelname)s: %(message)s" )
        return

    def startup(self):
        random.seed()
        pygame.init()
        self.services = Services()
        self.services.readyVideo( 320, 240 )
        self.gameModes = {}
        self.gameModes["load"] = LoadScreen(self.services)
        self.gameModes["menu"] = MenuScreen(self.services)
        self.state = self.gameModes["load"]

    def shutdown(self):
        pass

    def run(self):
        self.startup()
        while self.state != None:
            res = self.state.run()
            if res in self.gameModes:
                self.state = self.gameModes[res]
            else:
                self.state = None
        self.shutdown()
        return

# ----------------------------------------------------------------------------

def startGame():
    game = MainGame()
    game.run()

if __name__ == "__main__":
    startGame()

