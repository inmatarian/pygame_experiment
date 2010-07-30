#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import logging, pygame, random, os, ConfigParser
from logging import debug, info, warning, error, critical
from loadscreen import *
from menuscreen import *
from services import *

class MainGame(object):
    def __init__(self):
        logging.basicConfig( level=logging.DEBUG,
                             format="%(levelname)s: %(message)s" )
        return

    def readConfig(self):
        config = {}
        config["video.width"] = 320
        config["video.height"] = 240
        parser = ConfigParser.RawConfigParser()
        if os.path.exists("game.cfg"):
            parser.read("game.cfg")
            for s in parser.sections():
                for o in parser.options(s):
                    key = "%s.%s" % (s, o)
                    config[key] = parser.get( s, o )
                    debug("%s = %s" % (key, config[key]))
        return config

    def startup(self):
        random.seed()
        self.config = self.readConfig()
        pygame.init()
        self.services = Services()
        self.services.readyVideo( int(self.config["video.width"]), int(self.config["video.height"]) )
        self.gameModes = {}
        self.gameModes["load"] = LoadScreen(self.services)
        self.gameModes["menu"] = MenuScreen(self.services)
        self.state = self.gameModes["load"]

    def shutdown(self):
        debug( "FPS %s" % self.services.clock.get_fps() )

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

