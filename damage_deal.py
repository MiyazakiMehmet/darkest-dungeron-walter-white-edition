import pygame.sprite
from settings import *

class Damage(pygame.sprite.Sprite):
    def __init__(self,x,y,damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage,True,"red")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1

        cooldown = 20
        self.counter += 1

        if self.counter > cooldown:
            self.kill()

