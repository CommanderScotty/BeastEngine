import time
import pygame
from pygame.locals import *

from src.input.processInput import processInput
from src.updater.update import update
from src.renderer.render import render

from src.constants import *
from src.helpers import *

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Sample')
    showStartScreen(DISPLAYSURF, BASICFONT, FPSCLOCK)
    while True:
        mainloop()
        showGameOverScreen(DISPLAYSURF, BASICFONT)

def mainloop():
    prevTime = time.time()
    
    while(True):
        nowTime = time.time()
        elapsedTime = nowTime - prevTime
        prevTime = nowTime

        processInput()
        update(elapsedTime)
        render()
        rend()

def rend():
    DISPLAYSURF.fill(BGCOLOR)
    drawGrid(DISPLAYSURF)
    pygame.display.update()
    FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()
