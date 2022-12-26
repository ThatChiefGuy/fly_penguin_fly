import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image.set_colorkey((246, 246, 246))
