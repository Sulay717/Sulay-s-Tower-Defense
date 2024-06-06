import pygame
import os       
from pathlib import Path    
import constants as c
import enemy



money=0
spriteFolder = Path('Sprites')
pygame.init()
screen = pygame.display.set_mode((650,650))
pygame.Surface.fill(screen,(210,180,140))
pygame.display.update()
pygame.display.set_caption("Sulay's Tower Defense")
clock=pygame.time.Clock()
running = True
waypoints=[(25,50),(65,50),(65*2,50),(65*4,50),(325,600)]
pygame.draw.line(screen,(255, 255, 255),(0,50),(325,50),20)
pygame.draw.line(screen, (255,255,255), (325,40), (325,600), width=20)
#all_enemies = pygame.sprite.GroupSingle()
gameSprites = pygame.sprite.Group()

class Base(pygame.sprite.Sprite):
    def __init__(self,health,pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('sprites\Base.png')
        self.image = pygame.transform.scale(image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.center=pos
        self.health = health


def makeWaypoints(start,end):
    endPoint = end
    curr=start
    while curr[0] != end[0]:
        pass



playerHome = Base(200,(325,600))
Enemy1 = enemy.Enemy(waypoints)
x = Enemy1.pos[0]
y=Enemy1.pos[1]



#all_enemies = pygame.sprite.GroupSingle()

#all_enemies.add(Enemy1)
gameSprites.add(playerHome,Enemy1)

while running == True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")
                running=False

             
    gameSprites.draw(screen)
    Enemy1.update()
    pygame.display.flip() 