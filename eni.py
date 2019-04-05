import pygame
import random

WIDTH=500
HEIGHT=500


WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)


class En(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,30))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(30,WIDTH-60)
        self.rect.y=30
        self.tt=240
    def update(self):
        self.tt-=1
        if self.tt<0 :
            self.kill()
            self.tt=240
    def freez(self):
        self.tt+=150
        self.image.fill((200,200,0))

enn=pygame.sprite.Group()

