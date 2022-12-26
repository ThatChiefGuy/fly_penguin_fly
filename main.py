import pygame
import Player
import math


class Game:
    def __init__(self, window_size_x, window_size_y, title, fps):
        pygame.init()
        self.window_width = window_size_x
        self.window_height = window_size_y
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(title)
        self.Fps = fps
        back_ground = pygame.image.load("backgound.jpg").convert_alpha()
        self.back_ground = pygame.transform.scale(back_ground, (700, 350))
        self.back_ground_height = back_ground.get_height()
        self.tiles = math.ceil(self.window_height / self.back_ground_height) + 1
        self.scroll = 0

    def draw(self, draw_player):
        self.window.fill((43, 208, 237))

        for i in range(0, self.tiles):
            self.window.blit(self.back_ground, (0, i * self.back_ground_height + self.scroll))

        draw_player.player_group.draw(self.window)
        pygame.display.update()

    def main(self, draw_player):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.Fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.scroll -= 2
            if abs(self.scroll) > self.back_ground_height:
                self.scroll = 0

            self.draw(draw_player)
        pygame.quit()


game = Game(700, 900, "Snow bal fight ", 60)
player = Player.Player(100, 100, 300, 700)

if __name__ == "__main__":
    game.main(player)
