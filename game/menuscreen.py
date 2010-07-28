#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

from logging import debug, info, warning, error, critical
from gamemode import *

class MenuScreen(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services)

    def run(self):
        screen = self.services.screen
        background = pygame.Color(16, 16, 192, 255)
        rect = pygame.Rect(0, 0, 320, 240)
        pygame.draw.rect(screen, background, rect)
        pygame.display.flip()
        while True:
            self.delay()
        return None

