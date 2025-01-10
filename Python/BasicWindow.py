import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Untitled')
        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

    def run():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            clock.tick(60)

Game().run()