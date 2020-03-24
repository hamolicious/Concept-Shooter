
import colors
import pygame
from pygame.locals import *
from data_structures import Vector

import envir

class Player():
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.vel = Vector(0, 0)

        self.w = 20
        self.h = 40

        self.speed = 5

        self.jump_ready = True
        self.jump_pow = 70

        self.max_stamina = 15
        self.stamina = self.max_stamina

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)

    def show(self, screen):
        pygame.draw.rect(screen, colors.player, self.rect)

    def update(self, key, enemies):
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.w, self.h)

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and enemy.lethal : return True

        # region movement
        if key[K_a] : self.vel.x -= self.speed
        if key[K_d] : self.vel.x += self.speed
        if key[K_SPACE] and self.jump_ready:
            self.vel.y -= self.jump_pow
            self.jump_ready = False

        self.pos.add(self.vel)
        #endregion

        # region ground cases
        if self.pos.y + self.h < envir.ground:
            self.vel.y += envir.gravity
        else:
            self.pos.y = envir.ground - self.h
            self.jump_ready = True
            self.stamina = self.max_stamina
        #endregion

        # region wall cases
        # left
        if self.pos.x >= envir.size[0] - self.w:
            self.pos.x = envir.size[0] - self.w

            if self.stamina <= 0:
                self.vel.y *= 0.6
            else:
                self.vel.y = 0

            self.stamina -= 1

            if key[K_a] and not key[K_d]:
                self.jump_ready = True

        # right
        if self.pos.x <= 0:
            self.pos.x = 0

            if self.stamina <= 0:
                self.vel.y *= 0.6
            else:
                self.vel.y = 0

            self.stamina -= 1

            if key[K_d] and not key[K_a]:
                self.jump_ready = True
        #endregion

        # region top case

        if self.pos.y <= 0:
            self.pos.y = 0

            if self.vel.y < 0:
                self.vel.y *= -1

        #endregion

        self.vel.mult(0.8)
