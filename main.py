import pygame
import os       
from pathlib import Path    
import World
import constants as c
from menu import Menu
from turret import Turret
import enemy
import json


#core game features that need to be initationed 
money=0
spriteFolder = Path('Sprites')
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_HEIGHT,c.SCREEN_WIDTH))
pygame.Surface.fill(screen,(210,180,140))
pygame.display.update()
pygame.display.set_caption("Sulay's Tower Defense")
clock=pygame.time.Clock()
running = True

#create groups
enemy_sprites = pygame.sprite.Group()

#load images
enemy_image = open('sprites/enemy_1.png')
world_image = open('levels/level.png')
menu_image=open('assets/menu.png')




class Base(pygame.sprite.Sprite):
    def __init__(self,health,pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('sprites/Base.png').convert_alpha()
        self.image = pygame.transform.scale(image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center=pos
        self.health = health

#open the level data map and grab waypoint file
with open('levels/level.tmj') as file:
    world_data = json.load(file)

#create world map and process data
map = World.World(world_data,world_image)
map.process_data()
menu = Menu(menu_image)



#creating enemy
Enemy = enemy.Enemy(map.waypoints,enemy_image)




#all_enemies = pygame.sprite.GroupSingle()

#all_enemies.add(Enemy1)
enemy_sprites.add(Enemy)

#game loop
while running == True:
    #Core game functions, FPS, screen filling and drawing the map.
    clock.tick(c.FPS)
    screen.fill((210,180,140))
    map.draw(screen)

    
    enemy_sprites.update()      
    enemy_sprites.draw(screen)

    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")   
                running=False



pygame.quit()