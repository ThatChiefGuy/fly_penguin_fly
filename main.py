import pygame


class Game:
    def __init__(self, window_size_x, window_size_y, title, fps):
        self.window = pygame.display.set_mode((window_size_x, window_size_y))
        pygame.display.set_caption(title)
        self.Fps = fps

    def draw(self):
        self.window.fill((195, 231, 55))
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(self.Fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
        pygame.quit()


game = Game(600, 800, "Snow bal fight ", 60)
if __name__ == "__main__":
    game.main()
