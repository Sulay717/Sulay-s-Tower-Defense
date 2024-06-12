import pygame
import os       
from pathlib import Path    
import World
import constants as c
import enemy
import json



money=0
spriteFolder = Path('Sprites')
pygame.init()
screen = pygame.display.set_mode((c.height,c.width))
pygame.Surface.fill(screen,(210,180,140))
pygame.display.update()
pygame.display.set_caption("Sulay's Tower Defense")
clock=pygame.time.Clock()
running = True
#all_enemies = pygame.sprite.GroupSingle()
enemy_sprites = pygame.sprite.Group()

class Base(pygame.sprite.Sprite):
    def __init__(self,health,pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('sprites/Base.png').convert_alpha()
        self.image = pygame.transform.scale(image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center=pos
        self.health = health


with open('levels/level.tmj') as file:
    world_data = json.load(file)

#playerHome = Base(200,(325,600))
world_map = World.World(world_data,'C:/Users/sbah/Sulay_TD/Sulay-s-Tower-Defense/levels/level.png')
world_map.process_data()

Enemy = enemy.Enemy(world_map.waypoints)


world_map.process_data()



#all_enemies = pygame.sprite.GroupSingle()

#all_enemies.add(Enemy1)
enemy_sprites.add(Enemy)

while running == True:
    clock.tick(c.FPS)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")   
                running=False

    screen.fill((210,180,140))
    world_map.draw(screen)

    pygame.draw.lines(screen, "grey0", False, world_map.waypoints, width=1)
    
    enemy_sprites.update()      
    enemy_sprites.draw(screen)

    pygame.display.flip() 



pygame.quit()