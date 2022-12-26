import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, starting_x, starting_y):
        super().__init__()
        self.image = pygame.image.load(
            "toppng.com-white-penguin-flying-club-penguin-flying-pengui-962x768.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey((246, 246, 246))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)
        self.rect = self.image.get_rect()
        self.rect.y = starting_y
        self.rect.x = starting_x
