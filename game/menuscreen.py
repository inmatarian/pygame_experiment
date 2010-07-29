#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

from logging import debug, info, warning, error, critical
from gamemode import *

class MenuScreen(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services, pygame.Color(16,16,192))

    def run(self):
        while True:
            self.delay()
        return None

