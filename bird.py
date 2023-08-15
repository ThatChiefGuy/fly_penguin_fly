import pygame
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_group, size, window_size):
        super().__init__()
        self.side = random.choice(["left", "right"])
        self.window_size_x, self.window_size_y = window_size
        self.image = pygame.surface.Surface(size)
        self.rect = self.image.get_rect()

        if self.side == "right":
            self.image_list = [pygame.transform.scale(pygame.image.load("bird_frames/Frame-1.png"), size),
                               pygame.transform.scale(pygame.image.load("bird_frames/Frame-2.png"), size),
                               pygame.transform.scale(pygame.image.load("bird_frames/Frame-3.png"), size),
                               pygame.transform.scale(pygame.image.load("bird_frames/Frame-4.png"), size)
                               ]
            self.rect.center = 0 - self.rect.width, random.randint(150, self.window_size_y - 150)
        if self.side == "left":
            self.image_list = [pygame.transform.scale(
                               pygame.transform.flip(pygame.image.load("bird_frames/Frame-1.png"), True, False), size),
                               pygame.transform.scale(
                               pygame.transform.flip(pygame.image.load("bird_frames/Frame-2.png"), True, False), size),
                               pygame.transform.scale(
                               pygame.transform.flip(pygame.image.load("bird_frames/Frame-3.png"), True, False), size),
                               pygame.transform.scale(
                               pygame.transform.flip(pygame.image.load("bird_frames/Frame-4.png"), True, False), size),
                               ]
            self.rect.center = self.window_size_x, random.randint(150, self.window_size_y - 150)
        self.image = self.image_list[0]
        self.image = pygame.transform.scale(self.image, size)
        self.speed = 2
        self.velocity_x = 0
        self.velocity_y = -5
        self.flap_time = random.randint(40, 75)
        self.flap_timer = 0
        self.flap_velocity = -10
        self.animation_time = 0
        self.animation_timer = 20
        self.animation_increase = 1
        self.died = False
        bird_group.add(self)

    def update(self):
        self.movement()
        self.collisions()
        self.animation()

    def movement(self):
        self.flap_timer += 1
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.side == "left":
            self.velocity_x = -self.speed

        if self.side == "right":
            self.velocity_x = self.speed

        self.velocity_y += 0.3

        if self.flap_timer >= self.flap_time and self.died is False:
            self.flap_timer = 0
            self.flap_time = random.randint(50, 80)
            self.velocity_y = self.flap_velocity

    def animation(self):
        self.animation_time += self.animation_increase
        if self.animation_time < 0:
            self.animation_increase = 1

        if self.animation_time == 0:
            self.image = self.image_list[0]

        if self.animation_time == 5:
            self.image = self.image_list[1]

        if self.animation_time == 10:
            self.image = self.image_list[2]

        if self.animation_time == 15:
            self.image = self.image_list[3]
            self.animation_increase = -1

    def collisions(self):
        if self.rect.right < -40:
            self.kill()

        if self.rect.left > self.window_size_x + 40:
            self.kill()

        if self.rect.top > self.window_size_y + 100:
            self.kill()

        if self.died is True:
            self.animation_increase = 0
            print(self.died)

