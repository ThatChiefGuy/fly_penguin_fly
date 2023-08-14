import pygame
import Bird
import Player
import rock
import random
import math


class Game:
    def __init__(self, window_size_x, window_size_y, title, fps):
        pygame.init()
        self.window_height, self.window_width = window_size_x, window_size_y
        self.window_width = window_size_x
        self.window_height = window_size_y
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(title)

        self.Fps = fps
        self.rock_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()

        self.player = Player.Player(90, 90, 300, 100)
        self.rock = rock.Rock((30, 30), random.randrange(-20, -5), random.randrange(20, self.window_height - 100),
                              window_size_x, self.rock_group)
        self.bird = Bird.Bird(self.bird_group, (70, 60))

        back_ground = pygame.image.load("backgound.jpg").convert_alpha()
        self.back_ground = pygame.transform.scale(back_ground, (self.window_width, self.window_height))
        self.back_ground_height = back_ground.get_height()
        self.tiles = math.ceil(self.window_height / self.back_ground_height) + 1
        self.scroll = 0
        self.current_time = pygame.time.get_ticks()
        self.rock_last_spawn = 0
        self.rock_wait_time = 500

    def draw(self):
        self.window.fill((43, 208, 237))

        for i in range(0, self.tiles):
            self.window.blit(self.back_ground, (0, i * self.back_ground_height + self.scroll))

        # draws player hp
        pygame.draw.rect(self.window, (255, 0, 0), (10, 10, self.player.current_health / self.player.health_ratio, 25))
        pygame.draw.rect(self.window, (0, 0, 0), (10, 10, self.player.health_bar_length, 25), 4)

        self.player.player_group.draw(self.window)
        self.rock.rock_group.draw(self.window)
        self.bird_group.draw(self.window)
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.Fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.scroll -= 5
            self.current_time = pygame.time.get_ticks()

            if self.current_time - self.rock_last_spawn >= self.rock_wait_time:
                self.rock = rock.Rock((30, 30), random.randrange(-30, -10),
                                      random.randrange(100, self.window_height - 100),
                                      self.window_width, self.rock_group)

                self.rock_last_spawn = self.current_time

            if abs(self.scroll) > self.back_ground_height:
                self.scroll = 0

            key_input = pygame.key.get_pressed()
            self.player.movement(key_input)
            self.player.collisions(self.window_width, self.window_height)
            self.player.collisions_rock(self.rock_group)
            self.rock.rock_group.update()
            self.bird_group.update()

            self.draw()
        pygame.quit()


game = Game(1200, 900, "Fly penguin!", 60)

if __name__ == "__main__":
    game.main()
