
from math import sqrt
from random import randint

import pygame

import colors
import envir
from data_structures import Vector


class DotEnemy():
    def __init__(self):
        x = randint(0, envir.size[0])
        y = randint(0, 300)
        self.pos = Vector(x, y)
        self.w = 10
        self.h = 10
        self.speed = 5

        self.is_live = True
        self.lethal = True

        self.rect = pygame.Rect(x, y, self.w, self.h)

        self.health = 3

    def move_to_player(self, player_pos, enemies):
        dx = player_pos.x - self.pos.x
        dy = player_pos.y - self.pos.y

        vel = Vector(dx, dy)
        vel.normalise()
        vel.mult(self.speed)

        for enemy in enemies:
            if (d := sqrt((enemy.pos.x - self.pos.x)**2 + (enemy.pos.y - self.pos.y)**2)) > 0 and d < 50:
                diff = enemy.pos - self.pos
                diff.normalise()
                vel.sub(diff)

        self.pos.add(vel)

    def show(self, screen):
        pygame.draw.ellipse(screen, colors.red, self.rect)

    def update(self, player_pos, bullets, enemies):
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)
        self.move_to_player(player_pos, enemies)

        for bullet in bullets:
            if bullet.rect.colliderect(self.rect) : self.health -= 1
        
        if self.health <= 0:
            self.is_live = False
