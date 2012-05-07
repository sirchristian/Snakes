import pygame
from random import randint

class food:
    def __init__(self, game_surface):
        """ Represents a piece of snake food """
        game_rect = game_surface.get_rect()
        self.surface = pygame.Surface((15,15))
        self.surface.fill((randint(0x00, 0xff), 
                           randint(0x00, 0xff), 
                           randint(0x00, 0xff))) 
        self.pos = [randint(0,game_rect.width), randint(0,game_rect.height)]
        self.surface.scroll(self.pos[0], self.pos[1])
        game_surface.blit(self.surface, self.surface.get_rect())
        print 'Food placed at: {0}'.format(self.pos)

    def update(self, game_surface):
        """ Updates the food """
        rect = self.surface.get_rect().move(self.pos)
        game_surface.blit(self.surface, rect)

    def get_rect(self):
        return self.surface.get_rect().move(self.pos)

if __name__ == "__main__":
    # Or you could run unit tests...
    pass
