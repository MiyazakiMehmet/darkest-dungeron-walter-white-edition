from settings import *

class Healtbar:
    def __init__(self,x,y,hp,max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self,hp):
        #updated hp
        self.hp = hp
        #reduce the green rect
        ratio = self.hp / self.max_hp

        self.red_bar = pygame.draw.rect(WIN, "red", pygame.Rect(self.x,self.y,200,20))
        self.green_bar = pygame.draw.rect(WIN, "green", pygame.Rect(self.x,self.y,200*ratio, 20))