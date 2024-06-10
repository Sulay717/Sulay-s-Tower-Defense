import pygame
import os       
from pathlib import Path    
import constants as c
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self,waypoints):
        self.waypoints = waypoints
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("C:/Users/sbah/Sulay_TD/Sulay-s-Tower-Defense/sprites/mgMan.png")
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.image = pygame.transform.scale(image, (60,60))
        self.rect = self.image.get_rect()
        self.speed = 2
        #self.rect.fit(5,5,5,5)
        self.rect.center=self.pos       
        self.alive = True

    def update(self):
        self.move(self.waypoints)

    def move(self,waypoints):
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target-self.pos
        self.pos += self.movement.normalize() *self.speed
        self.rect.center=self.pos