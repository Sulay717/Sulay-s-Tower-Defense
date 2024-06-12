import pygame
import os       
from pathlib import Path    
import World
import constants as c
from menu import Menu
from turret import Turret
from enemy import Enemy
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
enemy_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()


#load images
enemy_image =  pygame.image.load(open('sprites/enemy_1.png')).convert_alpha()
world_image = pygame.image.load(open('levels/level.png')).convert_alpha()
menu_image=  pygame.image.load(open('assets/menu.png')).convert_alpha()
turret_image= pygame.image.load(open('assets/cursor_turret.png')).convert_alpha()




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


def create_turret(mouse_pos):
    mousetile_x = mouse_pos[0]//c.TILE_SIZE
    mousetile_y=mouse_pos[1]//c.TILE_SIZE
    mouse_tilenum = (mousetile_y*c.COLS)+mousetile_x
    #checks if the tile clicked on is grass
    if map.tilemap[mouse_tilenum]==7:
        #check if theres a turret
        space_is_free = True
        for turret in turret_group:
            if (mousetile_x,mousetile_y)==(turret.tile_x,turret.tile_y):
                space_is_free=False
            else:
                space_is_free==True

        if space_is_free==True:
            new_turret = Turret(world_data,turret_image,mousetile_x,mousetile_y)
            turret_group.add(new_turret)


#create world map and process data
map = World.World(world_data,world_image)
map.process_data()
menu = Menu(menu_image)



#creating enemy
enemy = Enemy(map.waypoints,enemy_image)




#all_enemies = pygame.sprite.GroupSingle()

#all_enemies.add(Enemy1)
enemy_group.add(enemy)

#game loop
while running == True:
    #Core game functions, FPS, screen filling and drawing the map.
    clock.tick(c.FPS)
    screen.fill((210,180,140))
    map.draw(screen)

    
    enemy_group.update()      
    enemy_group.draw(screen)
    turret_group.update()
    turret_group.draw(screen)

    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")   
                running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            #print("Mouse button 1")
            if pygame.mouse.get_pressed(5):
                mouse_pos = pygame.mouse.get_pos() 
                create_turret(mouse_pos)



pygame.quit()