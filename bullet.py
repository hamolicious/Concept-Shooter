
from data_structures import Vector
from math import sqrt
import colors
import pygame
import envir

class Bullet():
    def __init__(self, x, y, px, py):
        self.pos = Vector(x, y)
        self.speed = 10
        self.size = 5
        
        dx = px - x
        dy = py - y

        self.vel = Vector(dx, dy)
        self.vel.normalise()
        self.vel.mult(self.speed)

        self.is_live = True
        self.lethal = False
        self.to_die = False
        self.ttl = 100
        self.till_lethal = self.ttl - 20

        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

    def show(self, screen):
        if self.lethal:
            c = colors.bullet
        else:
            c = colors.non_lethal
        pygame.draw.circle(screen, c, (self.pos.x, self.pos.y), self.size)

    def update(self):
        self.pos.add(self.vel)
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)
        self.ttl -= 1

        if self.ttl < self.till_lethal:
            self.lethal = True

        if self.pos.x >= envir.size[0]:
            self.pos.x = envir.size[0]
            self.vel.x *= -1
            if self.to_die:
                self.is_live = False

        if self.pos.x <= 0:
            self.pos.x = 0
            self.vel.x *= -1
            if self.to_die:
                self.is_live = False

        if self.pos.y >= envir.ground:
            self.pos.y = envir.ground
            self.vel.y *= -1
            if self.to_die:
                self.is_live = False

        if self.pos.y <= 0:
            self.pos.y = 0
            self.vel.y *= -1
            if self.to_die:
                self.is_live = False

        if self.ttl <= 0:
            self.to_die = True
