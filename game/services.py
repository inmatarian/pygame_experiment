#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------
# Place for sticking crap. GameModes will share the services object

import sys, pygame
from logging import debug, info, warning, error, critical

class Services(object):
    def __init__(self):
        self.screen = None
        self.video_offset = (0,0)
        self.fonts = {}
        self.fonts["monospace_small"] = pygame.font.Font("data/FreeMono.ttf", 16)
        self.fonts["monospace_big"] = pygame.font.Font("data/FreeMono.ttf", 32)

    def getNextEvent(self):
        key = None
        modifier = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                self.readyVideo( event.w, event.h )
                self.flipScreens()
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if len(key) == 3 and key[0] == '[' and key[2]==']':
                    key = key[1]
                elif len(key) == 1:
                    key = str(event.unicode[0:1])
                if event.mod & pygame.KMOD_CTRL:
                    modifier = "ctrl"
                elif event.mod & pygame.KMOD_ALT:
                    modifier = "alt"
                if key == "f10" or ( key == "f4" and modifier == "alt" ):
                    sys.exit()
        return key, modifier

    def readyVideo(self, width, height):
        self.video_surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        desired_ratio = 4.0 / 3.0
        actual_ratio = float(width) / float(height)
        if desired_ratio > actual_ratio:
            buffer_width = int(width / 80) * 80
            buffer_height = buffer_width / desired_ratio
        else:
            buffer_height = int(height / 60) * 60
            buffer_width = buffer_height * desired_ratio
        self.buffer_surface = pygame.Surface((buffer_width, buffer_height))
        self.video_offset = ( (width - buffer_width) / 2,
                              (height - buffer_height) / 2 )
        if self.screen == None:
            self.screen = pygame.Surface((320, 240))

    def flipScreens(self):
        self.video_surface.blit(
            pygame.transform.scale(self.screen,
                self.buffer_surface.get_size(), self.buffer_surface),
            self.video_offset)
        pygame.display.flip()

    def getTextSurface( self, face, text, aliased = True, color = (255,255,255) ):
        font = self.fonts[face]
        return font.render( text, aliased, pygame.Color(color[0], color[1], color[2]) )

