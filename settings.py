import pygame
pygame.font.init()
panel = 150
screen_width = 850
screen_height = 465 + panel

WIN = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60

#font
char_font = pygame.font.SysFont("comic sans",20)
font = pygame.font.SysFont("comic sans",28)

game_over = False