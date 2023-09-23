import pygame
import bird
import Player
import button
import rock
import random
import math
import present
import os
os.chdir("C:/Users/perop/Fly_penguin")


class Game:
    def __init__(self, window_size_x, window_size_y, title, fps):
        pygame.init()
        pygame.mixer.music.load("Assets/starting_screen_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        self.window_height, self.window_width = window_size_x, window_size_y
        self.window_width = window_size_x
        self.window_height = window_size_y
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(title)
        self.started = False
        self.restarted = False
        self.main_music_played = False
        self.Fps = fps
        self.rock_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.present_group = pygame.sprite.Group()

        self.player = Player.Player(100, 90, 600, 450, self.player_group)
        self.start_button = button.Button(pygame.image.load("Assets/start_button.png"), 600, 600, 0.3, self.window)
        self.restart_button = button.Button(pygame.image.load("Assets/restart_button.png"), 600, 700, 0.3, self.window)
        back_ground = pygame.image.load("Assets/backgound.jpg").convert_alpha()
        self.back_ground = pygame.transform.scale(back_ground, (self.window_width, self.window_height))
        self.back_ground_height = back_ground.get_height()
        self.tiles = math.ceil(self.window_height / self.back_ground_height) + 1
        self.scroll = 0
        self.current_time = pygame.time.get_ticks()
        self.rock_last_spawn = 0
        self.rock_wait_time = 1000
        self.bird_time = 5000
        self.bird_last_spawn = 0
        self.present_last_spawn = 0
        self.present_time = 10000
        self.game_death_font = pygame.font.Font("Assets/game_font.ttf", 200)
        self.game_score_font = pygame.font.Font("Assets/game_font.ttf", 80)
        self.game_name_font = pygame.font.Font("Assets/game_name_font.otf", 90)
        self.score = 0

    def draw(self):
        self.window.fill((43, 208, 237))

        for i in range(0, self.tiles):
            self.window.blit(self.back_ground, (0, i * self.back_ground_height + self.scroll))

        # draws player hp
        pygame.draw.rect(self.window, (255, 0, 0), (10, 10, self.player.current_health / self.player.health_ratio, 25))
        pygame.draw.rect(self.window, (0, 0, 0), (10, 10, self.player.health_bar_length, 25), 4)

        if self.player.is_alive is False:
            you_died_text_img = self.game_death_font.render("YOU DIED", True, (255, 0, 0))
            total_score_img = self.game_score_font.render(f"Total score:{self.score}", True, (0, 0, 0))
            self.window.blit(total_score_img, (340, 500))
            self.window.blit(you_died_text_img, (270, 200))
            self.restarted = self.restart_button.draw()

        if self.started is False:
            fly_penguin_img = self.game_name_font.render("Fly Penguin", True, (255, 0, 0))
            self.window.blit(fly_penguin_img, (100, 200))
            self.started = self.start_button.draw()

        if self.started is True and self.main_music_played is False:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("Assets/main_theme.mp3")
            pygame.mixer.music.play(-1)
            self.main_music_played = True

        score_text_img = self.game_score_font.render(f"{self.score}", True, (0, 0, 0))
        self.window.blit(score_text_img, (800, 0))
        self.player_group.draw(self.window)
        self.rock_group.draw(self.window)
        self.bird_group.draw(self.window)
        self.present_group.draw(self.window)
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
            if self.restarted is True:
                self.player.current_health = 1000
                self.player.is_alive = True
                self.player.rect.center = 600, 450
                self.score = 0
                self.player.velocity_y = 0
                self.restarted = False
                self.started = False
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load("Assets/starting_screen_music.mp3")
                pygame.mixer.music.play(-1, fade_ms=2000)
                self.main_music_played = False

            if self.current_time - self.rock_last_spawn >= self.rock_wait_time and self.started is True:
                rock.Rock((30, 30), random.randrange(-30, -10),
                          random.randrange(100, self.window_height - 100),
                          self.window_width, self.rock_group)

                self.rock_last_spawn = self.current_time

            if self.current_time - self.bird_last_spawn >= self.bird_time and self.started is True:
                bird.Bird(self.bird_group, (70, 60), (self.window_width, self.window_height))
                self.bird_last_spawn = self.current_time

            if self.current_time - self.present_last_spawn >= self.present_time and self.started is True:
                present.Present(self.present_group, random.randrange(0, self.window_width))
                self.present_last_spawn = self.current_time

            if abs(self.scroll) > self.back_ground_height:
                self.scroll = 0
            if self.started is True:
                key_input = pygame.key.get_pressed()
                self.player_group.update(key_input, (self.window_width, self.window_height), self.rock_group, self.bird_group, self.player_group, self.present_group)
            self.rock_group.update()
            self.bird_group.update(self.player_group)
            self.present_group.update()
            self.draw()
            if self.player.is_alive is True and self.started is True:
                self.score += 1
        pygame.quit()


game = Game(1200, 900, "Fly penguin!", 60)

if __name__ == "__main__":
    game.main()
