import pygame
from pygame import Rect

class snake:
    def __init__(self,color,pos=[0,0]):
        """ A snake is a basic pygame.Rect that knows how to move around the
            screen and eat stuff """
        self.surface = pygame.Surface((30,30))
        self.surface.fill(color)
        self.pos = pos
        self.surface.scroll(pos[0], pos[1])

    def update(self, game_surface):
        """ Draws the snake onto the given surface """
        rect = self.surface.get_rect()
        game_surface.blit(self.surface, rect)

    def move(self, key, game_surface):
        """ Moves the snake based on the keys passed in """
        rect = self.surface.get_rect()
        if (key == pygame.K_UP):
            self.pos[1] = self.pos[1] - 10
        elif (key == pygame.K_DOWN):
            self.pos[1] = self.pos[1] + 10
        elif (key == pygame.K_LEFT):
            self.pos[0] = self.pos[0] - 10
        elif (key == pygame.K_RIGHT):
            self.pos[0] = self.pos[0] + 10

        # move the rectange to the position
        rect.move_ip(self.pos)

        # draw the rect on to our surface
        game_surface.blit(self.surface, rect)
        
if __name__ == "__main__":
    # Or you could run unit tests...
    pass
