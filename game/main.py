#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import logging, pygame, random
from logging import debug, info, warning, error, critical
from loadscreen import *
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
        self.state = LoadScreen(self.services)

    def shutdown(self):
        pass

    def run(self):
        self.startup()
        while self.state != None:
            self.state = self.state.run()
        self.shutdown()
        return

# ----------------------------------------------------------------------------

def startGame():
    game = MainGame()
    game.run()

if __name__ == "__main__":
    startGame()

