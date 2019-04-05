import pygame
from mi import *
GREEN=(0,255,0)
WIDTH=500
HEIGHT=500


all_sprites=pygame.sprite.Group()
bullets=pygame.sprite.Group()
abullets=pygame.sprite.Group()

class Spaceship(pygame.sprite.Sprite):
     def __init__(self):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.Surface((30,30))
         self.image.fill(GREEN)
         self.rect  = self.image.get_rect()
         self.rect.centerx=WIDTH/2
         self.rect.y=HEIGHT-60

     def update(self):
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_d]:
          if self.rect.x<WIDTH-60:
              self.rect.x+=30
       if keystate[pygame.K_a]:
          if self.rect.x>30:
              self.rect.x-=30

     def shoot1(self):
         bullet=smiss(self.rect.centerx,self.rect.y)
         all_sprites.add(bullet)
         bullets.add(bullet)

     def shoot2(self):
         bullet=amiss(self.rect.centerx,self.rect.y)
         all_sprites.add(bullet)
         abullets.add(bullet)
