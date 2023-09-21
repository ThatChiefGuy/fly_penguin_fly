import pygame


class Button:
    def __init__(self, image, x, y, scale, screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.screen = screen
        self.clicked = False

    def draw(self):
        action = False
        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position) and pygame.mouse.get_pressed()[0] is True:
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

