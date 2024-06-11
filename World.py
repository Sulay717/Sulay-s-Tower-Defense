import pygame

class World(pygame.sprite.Sprite):
    def __init__(self,world_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(world_image).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self,surface):
        surface.blit(self.image,(0,0))