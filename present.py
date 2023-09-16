import pygame
import random


class Present(pygame.sprite.Sprite):
    def __init__(self, present_group, x):
        super().__init__()
        self.type = random.choice(["speed", "health"])
        if self.type == "health":
            self.image = pygame.image.load("health_present.png")
        if self.type == "speed":
            self.image = pygame.image.load("speed_present.png")
        self.rect = self.image.get_rect()
        self.rect.y = -10
        self.rect.x = x
        self.speed = 5
        present_group.add(self)

    def update(self):
        self.movement()

    def movement(self):
        self.rect.y += self.speed
