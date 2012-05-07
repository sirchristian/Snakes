import pygame
from random import randint
from myobjects.snake import snake
from myobjects.food import food

# Settings
SCREENSIZE = (1024,768)
BGCOLOR = (0xff, 0xa5, 0x00)
FRAMERATE = 30

def playGame():
    print ('Starting Python Game...')

    # define the arrow keys
    arrow_keys = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    # init pygame
    pygame.init()
    game_surface = pygame.display.set_mode(SCREENSIZE)
    # set the key repeat speed
    pygame.key.set_repeat(10, 25)

    # create our snake
    python = snake(pygame.Color('purple'), 
            [randint(0,SCREENSIZE[0]), randint(0,SCREENSIZE[1])])
    python.update(game_surface)
   
    # create some food
    food_items = [food(game_surface)]

    game_clock = pygame.time.Clock()
    playing = True
    while playing:
        game_clock.tick(FRAMERATE)

        # reset surface to the background color
        game_surface.fill(BGCOLOR)

        # handle events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                playing = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    playing = False
                if e.key in arrow_keys:
                    python.move(e.key,game_surface)

        python.try_eat(food_items)
        if (len(food_items) < 1):
            food_items.append(food(game_surface))

        # update display & objects
        python.update(game_surface)
        for f in food_items:
            f.update(game_surface)
        pygame.display.update()

if __name__ == '__main__':
    playGame()
