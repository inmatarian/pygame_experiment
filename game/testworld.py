#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import random
from logging import debug, info, warning, error, critical
from gamemode import *
from freetravel import *

class TestWorld(FreeTravel):

    def __init__(self, services):
        FreeTravel.__init__(self, services)

    def initLevel(self):
        lev = LevelMap(40, 30)
        for x in xrange(40):
            lev.set(x, 0,  1)        
            lev.set(x, 29, 1)        
        for y in xrange(30):
            lev.set(0,  y, 1)
            lev.set(39, y, 1)
        self.setLevelMap(lev)

        floorColor = pygame.Color(16, 32, 64)
        floor = pygame.Surface((16,16))
        floor.fill(floorColor)
        wallColor = pygame.Color(192, 32, 32)
        wall = pygame.Surface((16,16))
        wall.fill(wallColor)
        tiles = [ floor, wall ]
        self.setLevelTiles(tiles)

