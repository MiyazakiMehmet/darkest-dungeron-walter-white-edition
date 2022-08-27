import pygame
from settings import *

class Buttons:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x_heal = 160
        self.y_heal = screen_height - panel - 180
        self.vel = 3
        self.clicked = True
        attack_img = pygame.image.load('attack.png')
        heal_potion_img = pygame.image.load('heal_pot.png')
        self.heal_potion_img = pygame.transform.scale(heal_potion_img, (40, 40))
        self.rect_healpot = heal_potion_img.get_rect()
        self.rect_healpot.bottomleft = [self.x+360,self.y + 474]
        self.attack_img = pygame.transform.scale(attack_img, (40, 40))
        self.rect = self.attack_img.get_rect()
        self.rect.bottomleft = [self.x,self.y]
        self.active = True
        self.clicked_pot = False
        self.pot_used = False
        self.font = pygame.font.SysFont("comic sans",30)
        self.render = self.font.render("+20",True,"green")

    def click(self,name,enemy,enemy1,enemy2):
        pos = pygame.mouse.get_pos()

        if self.clicked and self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.clicked = False
            self.active = True
        if not self.clicked:
            name.attack(enemy,enemy.rect.left - 150,enemy1,enemy2)
            if name.rect.x <= 80:
                self.clicked = True
                self.active = False

    def pot(self,name):
        pos = pygame.mouse.get_pos()

        if not self.clicked_pot and self.rect_healpot.collidepoint(pos) and pygame.mouse.get_pressed()[0]\
                and not self.pot_used and name.turn:
            self.clicked_pot = True
            self.active = True
        if self.clicked_pot and name.potions <= 3 and name.potions > 0 and name.hp < 100 and name.turn\
                and  self.pot_used == False:
            if name.hp >= 80:
                name.hp = 100
            else:
                name.hp += 20
            name.potions -= 1
            self.clicked_pot = False
            self.active = False
            self.pot_used = True

    def draw(self,win):
        win.blit(self.attack_img, self.rect)
        win.blit(self.heal_potion_img, self.rect_healpot)
        if self.pot_used and self.y_heal >= 240:
            win.blit(self.render,(self.x_heal -10,self.y_heal -10))
            self.y_heal -= self.vel
