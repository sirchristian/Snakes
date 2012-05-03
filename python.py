import pygame
from myobjects.snake import snake

# Settings
SCREENSIZE = (1024,768)
BGCOLOR = (0x5e, 0x00, 0xaa)

def playGame():
    print ('Starting Python Game...')

    arrow_keys = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    # init pygame
    pygame.init()
    game_surface = pygame.display.set_mode(SCREENSIZE)
    game_surface.fill(BGCOLOR)

    # create our snake
    python = snake(pygame.Color('white'))
    python.update(game_surface)
    playing = True
    while playing:
        # handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                playing = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    playing = False
                if e.key in arrow_keys:
                    python.move(e.key,game_surface)


        # update display            
        pygame.display.update()


if __name__ == '__main__':
    playGame()
