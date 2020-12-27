import pygame

class GameObject:
    def __init__(self, color):
        self.position = [50.0, 50.0]
        self.dimension = [40.0, 60.0]
        self.maxVel = 700.0
        self.color = color

    def update(self, tDelta, actions):
        if actions['moveUp']:
            self.position[1] -= self.maxVel * tDelta
        if actions['moveDown']:
            self.position[1] += self.maxVel * tDelta
        if actions['moveLeft']:
            self.position[0] -= self.maxVel * tDelta
        if actions['moveRight']:
            self.position[0] += self.maxVel * tDelta

    def render(self, win):
        pygame.draw.rect(win, 
                self.color, 
                (self.position[0], 
                    self.position[1], 
                    self.dimension[0], 
                    self.dimension[1]))
     
