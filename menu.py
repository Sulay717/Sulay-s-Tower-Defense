import pygame

class Menu():
    def __init__(self,image):
        o_image = image
        self.image = pygame.transform.scale(o_image,(5,5))
        self.active = False
        
    def draw(self,surface):
        if self.active == True:
            self.image = pygame.transform.scale(self.image,(320,90))
            surface.blit(self.image,(200,600))
        