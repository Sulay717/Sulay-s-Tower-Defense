import pygame
import os       
from pathlib import Path    
import constants as c
from pygame.math import Vector2
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self,waypoints,image):
        self.waypoints = waypoints
        pygame.sprite.Sprite.__init__(self)
        self.origin_image = pygame.image.load(image).convert_alpha()
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.angle = 0
        self.speed = 2
        self.image = pygame.transform.rotate(self.origin_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center=self.pos       

    #updates enemy position and rotates it accordingly
    def update(self):
        self.move(self.waypoints)
        self.rotate()

    def move(self,waypoints):
        #if it's not at the last point it will continue to move
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target-self.pos
        else:
            self.kill()

        #checks distance
        dist = self.movement.length()
        
        if dist >= self.speed:
            self.pos += self.movement.normalize()*self.speed
        else:
            if dist!=0:
                self.pos+=self.movement.normalize()* dist
            self.target_waypoint+=1


    def rotate(self):
        #calculate distance
        dist=self.target-self.pos
        #use distance to calculate the angle
        self.angle =  math.degrees(math.atan2(-dist[1],dist[0]))
        self.image = pygame.transform.rotate(self.origin_image,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center=self.pos