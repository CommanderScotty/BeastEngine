import pygame
import time
from src.engineSettings import *
from src.gameObject import GameObject

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("game")

prevTime = time.time()
run = True
character = GameObject(YELLOW)

def checkInput():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        actions['moveLeft'] = True
    else:
        actions['moveLeft'] = False
    
    if keys[pygame.K_RIGHT]:
        actions['moveRight'] = True
    else:
        actions['moveRight'] = False

    if keys[pygame.K_UP]:
        actions['moveUp'] = True
    else:
        actions['moveUp'] = False

    if keys[pygame.K_DOWN]:
        actions['moveDown'] = True
    else:
        actions['moveDown'] = False
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()


def update(elapsedTime):
    character.update(elapsedTime, actions)


def render():
    win.fill(BLACK)
    character.render(win)
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Max 1000 frames per second.  Otherwise rounding error may cause elapsedTime to be 0.0
    pygame.time.delay(1)
    nowTime = time.time()
    elapsedTime = nowTime - prevTime
    prevTime = nowTime
    
    checkInput() 
    update(elapsedTime)
    render()
pygame.quit()
