from settings import *
from damage_deal import *

#assignments
damage_deal_group = pygame.sprite.Group()

import random
class Knight:
    def __init__(self,x,y,name,hp,strength,potions):
        self.x = 400
        self.turn = True
        self.vel = 40
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.alive = True
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.index = 0
        self.counter = 0
        self.images = []
        self.count = 0
        self.attacked = True
        self.spawn = True
        self.temp_image = []
        for i in range(8):
            img = pygame.image.load(f'HeroKnight_Idle_{i}.png')
            img = pygame.transform.scale(img, (240,130))
            self.temp_image.append(img)
        self.images.append(self.temp_image)
        self.temp_image = []
        for i in range(6):
            img = pygame.image.load(f'HeroKnight_Attack1_{i}.png')
            img = pygame.transform.scale(img, (240, 130))
            self.temp_image.append(img)
        self.images.append(self.temp_image)
        self.temp_image = []
        for i in range(3):
            img = pygame.image.load(f'HeroKnight_Hurt_{i}.png')
            img = pygame.transform.scale(img, (240, 130))
            self.temp_image.append(img)
        self.images.append(self.temp_image)
        self.temp_image = []
        for i in range(10):
            img = pygame.image.load(f'HeroKnight_Death_{i}.png')
            img = pygame.transform.scale(img, (240, 130))
            self.temp_image.append(img)
        self.images.append(self.temp_image)
        self.image = self.images[self.count][self.index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x,y]
        self.game_over = False

    def attack(self,target,enemy_x,enemy1,enemy2):

        rand = random.randint(-10, 10)
        self.damage = self.strength + rand

        damage_deal_text = Damage(target.rect.x +55,target.rect.y,str(self.damage))

        if enemy1.alive or enemy2.alive:
            if self.rect.x < enemy_x and self.attacked:
                self.rect.x += self.vel
            if self.rect.x >= enemy_x and self.attacked:
                if target.hp > 0:
                    target.hp -= self.damage
                    damage_deal_group.add(damage_deal_text)
                    target.index = 0
                    target.count = 2
                if target.hp <= 0:
                    target.hp = 0
                    target.alive = False
                self.count = 1
                self.index = 0
                self.attacked = False
                self.spawn = True
            if self.spawn and self.index >= 4:
                self.rect.x -= self.vel
                if self.rect.x < 80:
                    self.spawn = False
                    self.attacked = True
                    self.turn = False
                    if enemy1.alive:
                        enemy1.turn = True


    def draw(self,win):
        win.blit(self.image,self.rect)
        if self.attacked is False:
            damage_deal_group.draw(win)
            damage_deal_group.update()


    def update(self):
        cooldown = 6
        self.counter += 1
        if not self.game_over:
            if self.counter > cooldown:
                self.counter = 0
                self.index += 1
                if self.alive:
                    if self.index >= len(self.images[self.count]):
                        self.index = 0
                        self.count = 0
                if not self.alive:
                        self.count = 3
                        if self.index >= 8:
                            self.game_over = True


        self.image = self.images[self.count][self.index]