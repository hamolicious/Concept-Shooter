from random import randint

import pygame

import colors
import envir
from bullet import Bullet
from data_structures import Vector
from enemies import *
from player import Player

player = Player(50, envir.ground-60)

mouse = pygame.image.load('data/mouse/pointer.png')

# gun vars
global fire_rate, max_fire_rate, bullets

# enemy vars
global enemies, wave

def reset_vars():
    global fire_rate, max_fire_rate, bullets
    global enemies, wave

    bullets = []
    max_fire_rate = 5
    fire_rate = max_fire_rate

    enemies = [DotEnemy()]
    wave = 1

    player.pos = Vector(50, envir.ground-60)

reset_vars()

def game(screen):
    # region import globals and setup controlls
    global fire_rate, max_fire_rate, bullets
    global enemies, wave

    pygame.mouse.set_visible(False)

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = Vector(mouse_pos[0], mouse_pos[1])
    mouse_pressed = pygame.mouse.get_pressed()

    screen.fill(colors.black)
    #endregion

    # region player controlls
    if player.update(key, enemies + bullets) == True:
        reset_vars()
        screen.fill(colors.white)
        pygame.display.update()
        return 'gameover'
    player.show(screen)
    #endregion

    # region bullet controlls
    if mouse_pressed == (1,0,0) and fire_rate == max_fire_rate:
        bullets.append(Bullet(player.pos.x, player.pos.y, mouse_pos.x, mouse_pos.y))
        fire_rate = 0

    if fire_rate < max_fire_rate:
        fire_rate += 1

    temp = []
    for bullet in bullets:
        if bullet.is_live:
            bullet.update()
            bullet.show(screen)
            temp.append(bullet)
    bullets = temp
    #endregion

    # region enemy controlls
    temp = []
    for enemy in enemies:
        if enemy.is_live:
            enemy.update(player.pos, bullets, enemies)
            enemy.show(screen)
            temp.append(enemy)
    enemies = temp

    if len(enemies) == 0:
        wave += 1
        for _ in range(wave):
            enemies.append(DotEnemy())
    #endregion

    # region screen controlls
    pygame.draw.rect(screen , colors.brown, (0, envir.ground, envir.size[0], 50))
    screen.blit(mouse, (mouse_pos.x - 5, mouse_pos.y - 5))
    #endregion

    return 'game'
