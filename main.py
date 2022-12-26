import pygame
import Player


class Game:
    def __init__(self, window_size_x, window_size_y, title, fps):
        self.window = pygame.display.set_mode((window_size_x, window_size_y))
        pygame.display.set_caption(title)
        self.Fps = fps

    def draw(self, draw_player):
        self.window.fill((43, 208, 237))
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

            self.draw(draw_player)
        pygame.quit()


game = Game(700, 900, "Snow bal fight ", 60)
player = Player.Player(100, 100, 300, 700)

if __name__ == "__main__":
    game.main(player)
