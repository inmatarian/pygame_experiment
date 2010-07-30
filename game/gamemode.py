#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

import pygame
from logging import debug, info, warning, error, critical
from services import *

class GameMode(object):
    def __init__(self, services, backColor=pygame.Color(0,0,0)):
        self.services = services
        self.lastKey = None
        self.lastModkey = None
        self.group = pygame.sprite.LayeredDirty()
        self.background = pygame.Surface((320,240))
        self.background.fill( backColor )

    def run(self):
        pass

    def createSprite(self, image, rect, layer=0):
        s = pygame.sprite.DirtySprite()
        s.image = image
        s.rect = rect
        self.group.add( s, layer=layer )
        return s
    def hideSprite( self, sprite ):
        sprite.visible = 0
        sprite.dirty = 1
    def showSprite( self, sprite ):
        sprite.visible = 1
        sprite.dirty = 1
    def moveSprite( self, sprite, dx, dy ):
        sprite.rect.centerx += dx
        sprite.rect.centery += dy
        sprite.dirty = 1

    def delay(self, times=1):
        self.group.draw( self.services.screen, self.background )
        self.services.flipScreens()
        for i in range(times):
            pygame.time.wait(33)
        (self.lastKey, self.lastModkey) = self.services.getNextEvent()

