import pygame
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_group, size, position):
        super().__init__()
        self.image_list = [pygame.image.load("bird_frames/Frame-1.png"),
                           pygame.image.load("bird_frames/Frame-2.png"),
                           pygame.image.load("bird_frames/Frame-3.png"),
                           pygame.image.load("bird_frames/Frame-4.png"),
                           ]
        self.image = self.image_list[0]
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.side = random.choice(["left", "right"])

        bird_group.add(self)
