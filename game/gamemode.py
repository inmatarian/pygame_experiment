#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

from logging import debug, info, warning, error, critical
from services import *

class GameMode(object):
    def __init__(self, services):
        self.services = services
        self.lastKey = None

    def run(self):
        pass

    def delay(self, times=1):
        self.services.flipScreens()
        for i in range(times):
            pygame.time.wait(33)
        self.lastKey = self.services.getNextEvent()

