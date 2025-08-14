import pygame, random
from pygame.locals import * # type:ignore

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
GRAY = (220, 220, 220)
CLICKEDCOLOR = (100, 100, 100)

BGCOLOR = GRAY
BUTTONCOLOR1 = BLUE
BUTTONCOLOR2 = YELLOW
BUTTONCOLOR3 = GREEN
BUTTONCOLOR4 = RED
BUTTONCOLORS = [BUTTONCOLOR1, BUTTONCOLOR2, BUTTONCOLOR3, BUTTONCOLOR4]

WINDOWWIDTH = 600
WINDOWHEIGHT = 300
FPS = 30


def main():
    global FPS
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Memory Game")

    mouseX, mouseY = None, None

    while True:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouseClicked = True
                mouseX, mouseY = event.pos

        DISPLAYSURF.fill(BGCOLOR)
        drawButtons(BUTTONCOLORS)
        if mouseClicked:
            buttonClicked = checkButtonsClick(mouseX, mouseY)

            if buttonClicked[0]:
                showClick(buttonClicked[1])


def showClick(button):
    pass            

def drawButtons(colors):
    pass

def checkButtonsClick(mouseX, mouseY):
    pass

def playPattern():
    pass

def addNewPattern():
    pass

if __name__ == "__main__":
    main()