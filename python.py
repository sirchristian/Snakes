import pygame

# Settings
SCREENSIZE = (1024,768)
BGCOLOR = (0x5e, 0x00, 0xaa)

def playGame():
    print ('Starting Python Game...')

    # init pygame
    pygame.init()
    game_surface = pygame.display.set_mode(SCREENSIZE)
    game_surface.fill(BGCOLOR)

    playing = True
    while playing:
        # handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                playing = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    playing = False

        # update display            
        pygame.display.update()


if __name__ == '__main__':
    playGame()
