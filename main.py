import pygame
import os       
from pathlib import Path    


money=0
spriteFolder = Path('Sprites')
pygame.init()
screen = pygame.display.set_mode((650,650))
pygame.Surface.fill(screen,(210,180,140))
pygame.display.update()
pygame.display.set_caption("Sulay's Tower Defense")
clock=pygame.time.Clock()
running = True
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

        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("C:/Users/sbah/Sulay_TD/Sulay-s-Tower-Defense/sprites/mgMan.png")
        self.pos = (325,325)
        self.image = pygame.transform.scale(image, (60,60))
        self.rect = self.image.get_rect()
        #self.rect.fit(5,5,5,5)
        self.rect.center=self.pos       
        self.alive = True

playerHome = Base(200,(325,600))
Enemy1 = Enemy()

#all_enemies = pygame.sprite.GroupSingle()

#all_enemies.add(Enemy1)
gameSprites.add(playerHome,Enemy1)

while running == True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name=='tab':
                print("Tab has been pressed program is stopping")
                running=False
    pygame.event.wait(10)           
    gameSprites.draw(screen)
    pygame.display.flip() 