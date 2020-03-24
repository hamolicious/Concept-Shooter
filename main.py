
from time import sleep

import pygame

import envir
from game import game
from gameover import game_over
from menu import menu

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(envir.size)
clock, fps = pygame.time.Clock(), 30

stage = 'menu'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if stage == 'menu':
        stage = menu(screen)
    elif stage == 'game':
        stage = game(screen)
    elif stage == 'gameover':
        stage = game_over(screen)
    else:
        print('Unknown stage', stage)
        exit()

    pygame.display.update()
    clock.tick(fps)
