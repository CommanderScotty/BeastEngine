import pygame, sys, random
from pygame.locals import *
from .constants import *

def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}

def terminate():
    pygame.quit()
    sys.exit()

def checkCollision(entity0, entity1):
    for seg in entity0.coords:
        if entity1.coords[HEAD]['x'] == seg['x'] and entity1.coords[HEAD]['y'] == seg['y']:
            return True
    for seg in entity1.coords:
        if entity0.coords[HEAD]['x'] == seg['x'] and entity0.coords[HEAD]['y'] == seg['y']:
            return True
    return False

def showStartScreen(DISPLAYSURF, BASICFONT, FPSCLOCK):
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf = titleFont.render('AGENT SIMULATOR', True, PINK)
    degrees = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf = pygame.transform.rotate(titleSurf, degrees)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (math.floor(WINDOWWIDTH / 2), math.floor(WINDOWHEIGHT / 2))
        DISPLAYSURF.blit(rotatedSurf, rotatedRect)
        drawPressKeyMsg(DISPLAYSURF, BASICFONT)
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg(DISPLAYSURF, BASICFONT):
    pressKeySurf = BASICFONT.render('Press a key to play.', True, YELLOW)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showGameOverScreen(DISPLAYSURF, BASICFONT):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('SIMULATION', True, WHITE)
    overSurf = gameOverFont.render('TERMINATED', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (math.floor(WINDOWWIDTH / 2), 10)
    overRect.midtop = (math.floor(WINDOWWIDTH / 2), gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg(DISPLAYSURF, BASICFONT)
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return


def drawScore(entity, DISPLAYSURF, BASICFONT):
    scoreSurf = BASICFONT.render('Score: %s' % (entity.score), True, entity.color0)
    scoreRect = scoreSurf.get_rect()
    if entity.rank == 0:
        scoreRect.topleft = (10, 10)
    else:
        scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawGrid(DISPLAYSURF):
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))
