from settings import *
import pygame,random
from enemy import Enemy
from healtbar import Healtbar
from knight import Knight
from buttons import Buttons
from pygame import mixer
pygame.init()
mixer.init()
#load image
bg = pygame.image.load('bg_forest.png')


#assignments
enemy1 = Enemy(500,screen_height - panel - 62,"LightBandit","Bandit", 100,10,1)
enemy2 = Enemy(600,screen_height - panel - 62,"LightBandit","Bandit", 100,10,1)
char = Knight(100,screen_height - panel - 62,"Knight", 100,25,3)
hp_bar_char = Healtbar(106,screen_height - panel + 40,char.hp,char.max_hp)
hp_bar_enemy1 = Healtbar(525,screen_height - panel + 40,enemy1.hp,enemy1.max_hp)
hp_bar_enemy2  = Healtbar(525,screen_height - panel + 110,enemy2.hp,enemy2.max_hp)
buttons = Buttons(15,screen_height-33)
damage_deal_group = pygame.sprite.Group()
mixer.music.load("pokemon_song.mp3")
mixer.music.set_volume(0.05)
game_over = False


def font(win,text,color,pos):
    text = char_font.render(text,True,color)
    win.blit(text,pos)


def draw(win):
    win.blit(bg,(0,0))
    pygame.draw.rect(win, "sienna4",pygame.Rect(0,screen_height-panel,screen_width//2,panel))
    pygame.draw.rect(win, "sienna4", pygame.Rect(screen_width//2, screen_height - panel, screen_width // 2, panel))
    pygame.draw.line(win, "black",(screen_width//2,screen_height-panel),(screen_width//2,screen_height),6)
    char.draw(win)
    enemy1.draw(win)
    enemy2.draw(win)
    char.update()
    enemy1.update()
    enemy2.update()
    #text
    font(win,f'{char.name} HP: {char.hp}',"yellow",[140,screen_height-panel])
    font(win,f'{enemy1.name} HP: {enemy1.hp}',"orange",[560,screen_height-panel])
    font(win,f'{enemy2.name} HP: {enemy2.hp}', "orange",[560,screen_height-panel+74])
    #HP bar
    hp_bar_char.draw(char.hp)
    hp_bar_enemy1.draw(enemy1.hp)
    hp_bar_enemy2.draw(enemy2.hp)
    #buttons
    buttons.draw(win)
    #damage

    #screen update
    pygame.display.update()
    clock.tick(FPS)

running = True

if not game_over:
    mixer.music.play()
while running:

    keys = pygame.key.get_pressed()
    draw(WIN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    if not game_over:


        if enemy1.alive and enemy2.alive and char.turn and not enemy1.turn and not enemy2.turn:
            if enemy1.alive and enemy2.alive:
                random_list = [enemy1, enemy2]
                buttons.click(char, random.choice(random_list),enemy1,enemy2)

        if enemy1.alive:
            buttons.pot(char)

        if enemy2.alive:
            buttons.pot(char)

        if enemy1.turn or enemy2.turn:
            buttons.pot_used = False
            buttons.y_heal = screen_height - panel - 180
        if enemy1.alive == False and char.turn:
            buttons.click(char, enemy2,enemy1,enemy2)

        elif enemy2.alive == False and char.turn:
            buttons.click(char, enemy1,enemy1,enemy2)

        if not char.turn:
            if char.alive:
                if enemy1.turn  and enemy1.alive and not char.turn:
                    enemy1.attack(char,char.rect.right -120 ,500)
                    if enemy1.turn == False:
                        if enemy2.alive == False:
                            char.turn = True
                        else:
                            enemy2.turn = True
                if enemy1.alive == False:
                    enemy2.turn = True
                if enemy2.turn and not char.turn and enemy2.alive:
                    enemy2.attack(char, char.rect.right - 120 ,600)
                    if enemy2.turn == False:
                        char.turn = True

        if enemy1.alive == False and enemy2.alive == False:
            game_over = True

        elif char.alive == False:
            game_over = True


pygame.quit()

