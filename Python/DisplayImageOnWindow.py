import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Untitled')
        self.screen = pygame.display.set_mode((640,480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('Python/image.png')
        self.img.set_colorkey((0, 0, 0)) # for transparent background of images

        self.img_pos = [160, 260]
        self.movement = [False, False]



    def run(self):
        while True:
            self.screen.fill((14,219,248))
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5  # bool are converted to 0 or 1, true = 1, false = 0. 1 - 0 = 1, 1 - 1 = 0
            self.screen.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()