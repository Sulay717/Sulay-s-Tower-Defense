import pygame
import os       
from pathlib import Path    
import constants as c

class Enemy(pygame.sprite.Sprite):
    def __init__(self,waypoints):
        self.waypoints = waypoints
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("C:/Users/sbah/Sulay_TD/Sulay-s-Tower-Defense/sprites/mgMan.png")
        self.pos = self.waypoints[0]
        self.image = pygame.transform.scale(image, (60,60))
        self.rect = self.image.get_rect()
        #self.rect.fit(5,5,5,5)
        self.rect.center=self.pos       
        self.alive = True

    def update(self):
        self.move(self.waypoints)

    def move(self,waypoints):
        count=0
        self.rect.x=waypoints[count+1][0]