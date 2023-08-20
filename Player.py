import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, starting_x, starting_y, player_group):
        super().__init__()
        self.image = pygame.image.load(
            "player_image.png").convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey((246, 246, 246))
        self.rect = self.image.get_rect()
        self.rect.y = starting_y
        self.rect.x = starting_x
        self.velocity_x = 0
        self.velocity_y = 0
        self.control = True
        self.current_health = 1000
        self.maximum_health = 1000
        self.health_bar_length = 350
        self.health_ratio = self.maximum_health / self.health_bar_length
        player_group.add(self)

    def update(self, key_input, window_size, rock_group, bird_group):
        self.movement(key_input)
        self.collisions(window_size[0], window_size[1])
        self.collisions_rock(rock_group)
        self.collisions_bird(bird_group)

    def movement(self, key_input):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.control is True:
            if key_input[(ord("d"))]:
                self.velocity_x = 10

            if key_input[(ord("a"))]:
                self.velocity_x = -10

            if key_input[(ord("s"))]:
                self.velocity_y = 10

            if key_input[(ord("w"))]:
                self.velocity_y = -10

        if self.velocity_y < 0:
            self.velocity_y += 0.5

        if self.velocity_y > 0:
            self.velocity_y -= 0.5

        if self.velocity_x < 0:
            self.velocity_x += 0.5

        if self.velocity_x > 0:
            self.velocity_x -= 0.5

        if self.velocity_x == 0 and self.velocity_y == 0:
            self.control = True

    def collisions(self, window_width, window_height):
        if self.rect.x < 0:
            self.control = False
            self.velocity_x = 10

        if self.rect.right > window_width:
            self.control = False
            self.velocity_x = -10

        if self.rect.y < 0:
            self.control = False
            self.velocity_y = 10

        if self.rect.bottom > window_height:
            self.control = False
            self.velocity_y = -10

    def get_damage(self, amount):
        if self.current_health > 0 or not self.current_health == 0:
            self.current_health -= amount
        else:
            pass

    def get_health(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        else:
            self.current_health = self.maximum_health

    def collisions_rock(self, rock_group):
        if pygame.sprite.spritecollide(self, rock_group, True):
            self.get_damage(50)

    def collisions_bird(self, bird_group):
        if pygame.sprite.spritecollide(self, bird_group, False):
            if not pygame.sprite.spritecollide(self, bird_group, False)[0].died:
                self.get_damage(150)
                pygame.sprite.spritecollide(self, bird_group, False)[0].died = True
                pygame.sprite.spritecollide(self, bird_group, False)[0].velocity_y = -10
