import pygame

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

WIDTH=500
HEIGHT=500



class Mss(pygame.sprite.Sprite):
   def __init__(self,x,y,c,m):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((10,20))
       self.image.fill(c)
       self.rect=self.image.get_rect()
       self.rect.bottom=y
       self.rect.centerx=x
       self.speedy = m
   def update(self):
       self.rect.y +=self.speedy
       if self.rect.bottom<0:
          self.kill()

class smiss(Mss):
   def __init__(self,x,y):
      Mss.__init__(self,x,y,YELLOW,-10)

class amiss(Mss):
    def __init__(self,x,y):
        Mss.__init__(self,x,y,BLUE,-20)

