import pygame

class Menu():
    def __init__(self,image):
        o_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(o_image,(5,5))
        
    def draw(self,surface):
        self.image = pygame.transform.scale(self.image,(320,90))
        surface.blit(self.image,(200,600))