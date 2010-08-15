#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import random
from logging import debug, info, warning, error, critical
from gamemode import *

class LoadScreen(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services)

    def createLogoSprite(self):
        black = pygame.Color(0, 0, 0)
        logoSurf = self.services.getTextSurface( "default_big",
            "PLANETBADNESS", True, black )
        location = logoSurf.get_rect()
        location.center = self.services.screen.get_rect().center
        return self.createSprite( logoSurf, location, 1 )

    def waitOrKeys(self, timeout, keys):
        for i in range(timeout):
            self.delay()
            if self.lastKey in keys: return True
        return False

    def doAnimation(self):
        purple = pygame.Color(128, 16, 192)
        purpleBlock = pygame.Surface((20,20))
        purpleBlock.fill(purple)
        logo = self.createLogoSprite()
        self.hideSprite( logo ) 
        inblocks = []
        for y in range(12):
            for x in range(16):
                r = pygame.Rect( x * 20, y * 20, 20, 20 )
                sprite = self.createSprite( purpleBlock, r, 0 )
                self.hideSprite( sprite ) 
                inblocks.append( sprite )
        random.shuffle(inblocks)
        outblocks = []
        frames = 0
        killKeys = ("enter", "escape", "return")
        while len(inblocks) > 0:
            sprite = inblocks.pop()
            self.showSprite( sprite ) 
            outblocks.append(sprite)
            frames = (frames + 1) % 6
            if frames == 0:
                if self.waitOrKeys(1,killKeys): return
        if self.waitOrKeys(5,killKeys): return
        self.showSprite( logo ) 
        if self.waitOrKeys(25,killKeys): return
        frames = 0
        while len(outblocks) > 0:
            sprite = outblocks.pop()
            self.hideSprite( sprite ) 
            frames = (frames + 1) % 6
            if frames == 0:
                if self.waitOrKeys(1,killKeys): return
        if self.waitOrKeys(15,killKeys): return
        return

    def run(self):
        self.doAnimation()
        return "menu"

