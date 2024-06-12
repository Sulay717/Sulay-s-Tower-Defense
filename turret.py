import pygame

class Turret(pygame.sprite.Sprite()):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.pos = pos
        self.rect.center = pos
        
