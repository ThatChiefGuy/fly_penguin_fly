import random
import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.image.load("explosion-14272.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.timespan = 5

    def update(self):
        self.timespan -= 1
        if self.timespan <= 0:
            self.kill()


class Rock(pygame.sprite.Sprite):
    def __init__(self, size, velocity_y, starting_y, window_x, rock_group):
        super().__init__()
        self.size = size
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()
        self.rect.y = starting_y

        self.rock_group = rock_group
        self.rock_group.add(self)

        self.velocity_y = velocity_y
        self.velocity_x = -1

        self.sides = ["left", "right"]
        self.side = random.choice(self.sides)

        if self.side == "right":
            self.rect.x = window_x

    def explosion(self):
        print("ëxplosion happems")

        self.image = pygame.image.load("explosion-14272.png")

    def update(self):
        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x

        self.velocity_y += 0.5

        if self.side == "right":
            self.velocity_x -= 0.3
        else:
            self.velocity_x += 0.3


