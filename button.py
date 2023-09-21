import pygame.sprite


class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y,  button_group, action, resize=1,):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale_by(self.image, resize)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.action = action
        button_group.add(self)

    def update(self):
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0]:
            self.action = True

