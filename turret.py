import pygame
import constants as c

class Turret(pygame.sprite.Sprite):
    def __init__(self,data,image,tile_x,tile_y):
        pygame.sprite.Sprite.__init__(self)
        self.tilemap=[]
        self.data = data
        self.tile_x=tile_x
        self.tile_y=tile_y
        self.x=(self.tile_x+0.5)*c.TILE_SIZE
        self.y=(self.tile_y+0.5)*c.TILE_SIZE
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)

    #similar to the world class this processes the tmj file for the tilemap grid


    

        
