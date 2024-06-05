import pygame
import os

money=0

pygame.init()
screen = pygame.display.set_mode((10,10),pygame.SCALED)
pygame.Surface.fill(screen,(210,180,140))
pygame.display.update()
pygame.display.set_caption("Sulay's Tower Defense")
clock=pygame.time.Clock()
running = True

class Enemy(sprite):
    def _init_(self,pos,waypoints,alive):
        self.pos = (0,0)
        self.alive = True


""" while running == True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")
                running=False
    pygame.event.wait(10)    
    print("The game is running") """    