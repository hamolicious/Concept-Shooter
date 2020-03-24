
import pygame
from pygame.locals import K_SPACE

import colors
import envir


def menu(screen):
    key = pygame.key.get_pressed()

    screen.fill(colors.black)

    font = pygame.font.SysFont('ariel', 50)
    label = font.render('Press SPACE To Start', True, colors.white)
    w, h = label.get_size()
    screen.blit(label, (envir.size[0]/2 - w/2, envir.size[1]/2 - h/2))

    if key[K_SPACE]:
        return 'game'
    else:
        return 'menu'
