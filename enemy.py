import pygame.sprite, random
from damage_deal import *

damage_deal_group = pygame.sprite.Group()

class Enemy:
    def __init__(self,x,y,name,nickname,hp,strength,potions):
        self.turn = False
        self.vel = 40
        self.name = nickname
        self.hp = hp
        self.max_hp = hp
        self.index = 0
        self.alive = True
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.counter = 0
        self.attacked = True
        self.spawn = True
        self.images = []
        self.count = 0
        self.temp_img = []
        for i in range(4):
            image = pygame.image.load(f'{name}_Combat Idle_{i}.png')
            image = pygame.transform.scale(image,(120,120))
            self.temp_img.append(image)
        self.images.append(self.temp_img)
        self.temp_img = []
        for i in range(8):
            image = pygame.image.load(f'{name}_Attack_{i}.png')
            image = pygame.transform.scale(image,(120,120))
            self.temp_img.append(image)
        self.images.append(self.temp_img)
        self.temp_img = []
        for i in range(2):
            image = pygame.image.load(f'{name}_Hurt_{i}.png')
            image = pygame.transform.scale(image, (120, 120))
            self.temp_img.append(image)
        self.images.append(self.temp_img)
        self.temp_img = []
        image = pygame.image.load(f'{name}_Death_0.png')
        image = pygame.transform.scale(image, (120, 120))
        self.temp_img.append(image)
        self.images.append(self.temp_img)
        self.image = self.images[self.count][self.index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x,y]
        self.attack_counter = 0

    def attack(self, target, enemy_x,pos_x,):
        cooldown = 20
        self.attack_counter += 1
        rand = random.randint(-5,5)
        damage = self.strength + rand

        damage_deal = Damage(target.rect.x +115,target.rect.y,str(damage))

        if self.attack_counter > cooldown:
            if self.rect.left > enemy_x and self.attacked:
                self.rect.x -= self.vel
            if self.rect.left <= enemy_x +20 and self.attacked:
                if target.hp > 0:
                    target.hp -= damage
                    target.index = 0
                    damage_deal_group.add(damage_deal)
                    target.count = 2
                if target.hp <= 0:
                    target.hp = 0
                    target.alive = False
                self.count = 1
                self.index = 0
                self.attacked = False
                self.spawn = True
            if self.spawn and self.index >= 6:
                self.rect.x += self.vel
                if self.rect.x >= pos_x:
                    self.spawn = False
                    self.attacked = True
                    self.turn = False
                    self.attack_counter = 0

    def draw(self,win):
        win.blit(self.image,self.rect)
        if not self.attacked:
            damage_deal_group.draw(win)
            damage_deal_group.update()

    def update(self):
        cooldown = 6
        self.counter += 1
        if self.alive:
            if self.counter > cooldown:
                self.index += 1
                self.counter = 0
                if self.index >= len(self.images[self.count]):
                    self.index = 0
                    self.count = 0
        if not self.alive:
            self.index = 0
            self.count = 3
        self.image = self.images[self.count][self.index]