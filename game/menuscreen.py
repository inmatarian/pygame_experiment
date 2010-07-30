#
# See LICENSE.txt for Copyright and Licensing information.
#
# ----------------------------------------------------------------------------

from logging import debug, info, warning, error, critical
from gamemode import *

class MenuScreen(GameMode):
    def __init__(self, services):
        GameMode.__init__(self, services, pygame.Color(16,16,192))

    def createTextSprites(self):
        white = pygame.Color(255, 255, 255)
        screenRect = self.services.screen.get_rect()
        oldCenter = screenRect.center
        screenRect.height /= 2
        screenRect.width /= 2
        screenRect.center = oldCenter
        # GAME TITLE
        nameText = self.services.getTextSurface( "default_big",
            "GAME", True, white )
        nameRect = nameText.get_rect()
        nameRect.topleft = screenRect.topleft
        self.nameSprite = self.createSprite( nameText, nameRect, 1 )
        # QUIT MENU OPTION
        quitText = self.services.getTextSurface( "default_small",
            "Quit", True, white )
        quitRect = quitText.get_rect()
        quitRect.bottomright = screenRect.bottomright
        self.quitSprite = self.createSprite( quitText, quitRect, 1 )
        # PLAY MENU OPTION
        playText = self.services.getTextSurface( "default_small",
            "Play", True, white )
        playRect = playText.get_rect()
        playRect.bottomright = quitRect.topright
        self.playSprite = self.createSprite( playText, playRect, 1 )
        # CURSOR
        cursorText = self.services.getTextSurface( "default_small",
            "->", True, white )
        cursorRect = cursorText.get_rect()
        cursorRect.midright = playRect.midleft
        self.cursorSprite = self.createSprite( cursorText, cursorRect, 1 )
        return

    def menuGetOption(self):
        options = ( self.playSprite.rect.midleft, 
                    self.quitSprite.rect.midleft )
        results = ("play", "quit")
        debug( len(options) )
        opt = 0
        newOpt = 0
        while True:
            self.delay()
            if self.lastKey == "up" and opt > 0:
                newOpt -= 1
            elif self.lastKey == "down" and opt < len(options) - 1:
                newOpt += 1
            elif self.lastKey == "return":
                return results[opt]
            if newOpt != opt:
                (x, y) = self.cursorSprite.rect.midright
                (tx, ty) = options[newOpt]
                self.moveSprite( self.cursorSprite, tx - x, ty - y )
                opt = newOpt


    def run(self):
        self.createTextSprites()
        res = self.menuGetOption()
        debug(res)
        if res == "quit":
            return "quit"
        return "play"

