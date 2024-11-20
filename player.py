import pygame
from programmer import Programmer

class Player(Programmer):
    def __init__(self, x=50, y=540, balance=1000):
        self.x = x
        self.y = y
        self.balance = balance
        self.creativity = 50


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 5

        if keys[pygame.K_RIGHT]:
            self.x += 5

        if keys[pygame.K_UP]:
            self.y -= 5

        if keys[pygame.K_DOWN]:
            self.y += 5

    def pay(self):
        self.balance -= 10

    