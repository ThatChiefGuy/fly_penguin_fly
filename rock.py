import pygame


class Rock(pygame.sprite.Sprite):
    def __init__(self, size, starting_position):
        super().__init__()
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rock_group = pygame.sprite.Group()
        self.rock_group.add(self)
        self.rect.center = starting_position

