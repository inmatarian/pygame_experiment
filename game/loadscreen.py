#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import random
from logging import debug, info, warning, error, critical
from gamemode import *
from menuscreen import *

class LoadScreen(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services)

    def run(self):
        logo = self.services.getTextSurface( "monospace_big",
            "PLANETBADNESS", True, (0,0,0) )
        screen = self.services.screen
        purple = pygame.Color(128, 16, 192)
        black = pygame.Color(0, 0, 0)
        inblocks = []
        for y in range(12):
            for x in range(16):
                inblocks.append( pygame.Rect( x * 20, y * 20, 20, 20 ) )
        random.shuffle(inblocks)
        outblocks = []
        frames = 0
        while len(inblocks) > 0:
            rect = inblocks.pop()
            outblocks.append(rect)
            pygame.draw.rect(screen, purple, rect)
            frames = (frames + 1) % 6
            if frames == 0:
                self.delay()
        self.delay(5)
        location = logo.get_rect()
        location.center = screen.get_rect().center
        screen.blit( logo, location.topleft )
        self.delay(25)
        frames = 0
        while len(outblocks) > 0:
            rect = outblocks.pop()
            pygame.draw.rect(screen, black, rect)
            frames = (frames + 1) % 6
            if frames == 0:
                self.delay()
        self.delay(15)
        return MenuScreen(self.services)

