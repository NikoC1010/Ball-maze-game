import sys
import pygame
from GLOBAL import *
from pygame.locals import *
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(r''+path.path+'/picture/Q.png')
        self.pos=[100,100]
        self.rect=pygame.Rect(100,100,25,25)
        self.speed=2.8
        
    def move(self,map_group):
        kp=pygame.key.get_pressed()
        x = 0
        y = 0
        if kp[K_LEFT]:
            x -= self.speed
        elif kp[K_RIGHT]:
            x += self.speed
        if kp[K_UP]:
            y -= self.speed
        elif kp[K_DOWN]:
            y += self.speed

        self.pos[0] += x
        self.pos[1] += y

        if pygame.sprite.spritecollide(self, map_group, False) :

            self.pos = [100,100]

        if  self.rect.left< 50:

            self.pos = [100,100]
 
 
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
