#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import random, array
from logging import debug, info, warning, error, critical
from gamemode import *

# --------------------------------------

class LevelMap(object):
    def __init__(self, width, height, tilewidth=16, tileheight=16, defaultvalue=0):
        self.width = width
        self.height = height
        self.size = width * height
        self.tilewidth = tilewidth
        self.tileheight = tileheight
        self.defaultvalue = defaultvalue
        self.data = array.array( "L", [0 for i in xrange(self.size)] )

    def fill(self, val):
        for i in xrange( self.width * self.height ):
            self.data[i] = val

    def set(self, x, y, val):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        self.data[ (y * self.width) + x ] = val

    def get(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.defaultvalue
        return self.data[ (y * self.width) + x ]

    def render(self, screen, surfaces, camera_offset_x, camera_offset_y):
        sw = (screen.get_width() / self.tilewidth)
        sh = (screen.get_height() / self.tileheight)
        cx = camera_offset_x
        cy = camera_offset_y
        for y in xrange(sh):
            for x in xrange(sw):
                surf = surfaces[ self.get( cx + x, cy + y ) ]
                screen.blit( surf, ( x * self.tilewidth, y * self.tileheight ) )

# --------------------------------------

class FreeTravel(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services)

    def initLevel(self):
        pass

    def setLevelMap(self, ray):
        self.levelMap = ray

    def setLevelTiles(self, surfaces):
        self.tiles = surfaces

    def handleKeys(self):
        k = self.lastKey
        if k == "up":
            self.cy -= 1
        elif k == "down":
            self.cy += 1
        elif k == "left":
            self.cx -= 1
        elif k == "right":
            self.cx += 1

    def run(self):
        self.initLevel()
        self.cx = 0
        self.cy = 0
        while True:
            self.levelMap.render( self.services.screen, self.tiles, self.cx, self.cy )
            self.delay()
            self.handleKeys()

