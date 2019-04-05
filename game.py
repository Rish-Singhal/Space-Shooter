import pygame
import random
import os
pygame.font.init()
from os import path 

from sp import *
from mi import *
from eni import * 

WIDTH=500
HEIGHT=500
FPS=30

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders")
clock=pygame.time.Clock()

img_dir=path.join(path.dirname(__file__),'img')



WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

background=pygame.image.load(path.join(img_dir,"bg.png")).convert()
background_rect = background.get_rect()

fontObj =pygame.font.SysFont("Times New Roman,Ariel",30)
         

enn=pygame.sprite.Group()
spaceship=Spaceship()
all_sprites.add(spaceship)
running=True
cnt=300
score=0


while running:
     clock.tick(FPS)        
     for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                    spaceship.shoot1()
               if event.key == pygame.K_s:
                    spaceship.shoot2()
               if event.key ==pygame.K_q:
                    running=False
     if cnt==300 :
        en=En()
        all_sprites.add(en)
        enn.add(en)    
        cnt=0         
 
     all_sprites.update()
     hits=pygame.sprite.groupcollide(enn,bullets,True,True)
     for hit in hits : 
              score+=1
     hitm=pygame.sprite.groupcollide(enn,abullets,False,True)
     for hit in hitm:
              en.freez()
     text = fontObj.render("SCORE: "+str(score),True,WHITE)
     
     screen.fill(BLACK)
     screen.blit(background,background_rect)
     all_sprites.draw(screen)
     screen.blit(text ,( WIDTH/2 -text.get_rect().width/2, 0))
     pygame.display.flip()
     cnt+=1
     
