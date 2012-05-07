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
   
    # create the bad snake
    rattle = snake(pygame.Color('grey'), 
            [randint(0,SCREENSIZE[0]), randint(0,SCREENSIZE[1])])
    rattle.update(game_surface)
    rattle_num_frames_in_dir = 0
    rattle_max_frames_in_dir = 50
    rattle_dir = arrow_keys[randint(0,3)]

    # create some food
    food_items = []
    def create_food():
        while len(food_items) < 2:
            food_items.append(food(game_surface))

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

        # always move the bad snake
        rattle_num_frames_in_dir = rattle_num_frames_in_dir + 1
        moved_rattle = rattle_num_frames_in_dir % 2 == 0
        while not moved_rattle:
            if rattle_num_frames_in_dir > rattle_max_frames_in_dir:
                curr_dir = rattle_dir
                while curr_dir == rattle_dir:
                    rattle_dir = arrow_keys[randint(0,3)]
                rattle_max_frames_in_dir = randint(25,50)
                rattle_num_frames_in_dir = 0
            moved_rattle = rattle.move(rattle_dir,game_surface)
            if not moved_rattle:
                rattle_num_frames_in_dir = rattle_max_frames_in_dir+1

        # check to see if we collided with ourself, or the bad guy
        p_rects = python.get_rects()
        r_rects = rattle.get_rects()
        for x in range(len(p_rects)):
            self_collide = False
            for y in range(len(p_rects)):
                if x == y:
                    continue 
                if p_rects[x].inflate(-1,-1).colliderect(p_rects[y].inflate(-1,-1)):
                    self_collide = True
            rattle_collide = p_rects[x].collidelist(rattle.get_rects()) > -1
            if (self_collide or rattle_collide):
                print ("GAME OVER")
                playing = False

        # eat
        python.try_eat(food_items)
        rattle.try_eat(food_items)
        
        # replace food
        create_food()

        # update display & objects
        python.update(game_surface)
        rattle.update(game_surface)
        for f in food_items:
            f.update(game_surface)
        pygame.display.update()

if __name__ == '__main__':
    playGame()
