import pygame
from myobjects.food import food

class snake:
    SEGMENTSIZE = (30,30)

    def __init__(self,color,pos=[0,0]):
        """ A snake is a basic pygame.Rect that knows how to move around the
            screen and eat stuff """
        # create the head    
        head_surface = pygame.Surface(snake.SEGMENTSIZE)
        head_surface.fill(color)
        self._head = {'surface':head_surface,'pos':pos}

        # save of a new list of body segments
        self._segments = []

        # set the body color to be the inverse of the head
        self.color = pygame.Color(0xff-color.r, 0xff-color.g, 0xff-color.b, color.a)

    def _add_segment(self,pos):
        segment = pygame.Surface(snake.SEGMENTSIZE)
        segment.fill(self.color)
        segment.scroll(pos[0], pos[1])
        self._segments.append({'surface':segment,'pos':pos})

    def update(self, game_surface):
        """ Draws the snake onto the given surface """
        head_rect = self._head['surface'].get_rect()
        head_rect.move_ip(self._head['pos'])
        game_surface.blit(self._head['surface'], head_rect)

        for segment in self._segments:
            rect = segment['surface'].get_rect()
            rect.move_ip(segment['pos'])
            game_surface.blit(segment['surface'], rect)

    def move(self, key, game_surface):
        """ Moves the snake based on the keys passed in """

        game_rect = game_surface.get_rect()

        prev_segment_pos = self._head['pos'][:]

        # set the head position based on the key press
        if (key == pygame.K_UP):
            self._head['pos'][1] = self._head['pos'][1] - 30
        elif (key == pygame.K_DOWN):
            self._head['pos'][1] = self._head['pos'][1] + 30
        elif (key == pygame.K_LEFT):
            self._head['pos'][0] = self._head['pos'][0] - 30
        elif (key == pygame.K_RIGHT):
            self._head['pos'][0] = self._head['pos'][0] + 30
        else:
            return

        # make sure we don't go out of bounds
        head_rect = self._head['surface'].get_rect()
        max_x = game_rect.right - head_rect.width
        max_y = game_rect.bottom - head_rect.height
        position = [0 if self._head['pos'][0] < 0 else min(self._head['pos'][0], max_x),
                    0 if self._head['pos'][1] < 0 else min(self._head['pos'][1], max_y)] 

        # draw the head onto the surface
        head_rect.move_ip(position)
        game_surface.blit(self._head['surface'], head_rect)

        # update all the body segments to be in the position of its previous segment
        for segment in self._segments:
            saved_pos = segment['pos'][:]
            segment['pos'] = prev_segment_pos

            # draw the rect on to our surface
            rect = segment['surface'].get_rect()
            rect.move_ip(segment['pos'])
            game_surface.blit(segment['surface'], rect)
            prev_segment_pos = saved_pos


    def try_eat(self, food_items):
        """ Takes in a list of tasty treats. If the snake can eat it, it will """

        # get the head
        head_rect = self._head['surface'].get_rect()
        head_rect.move_ip(self._head['pos'])

        # see if the head collides with a food item
        for f in food_items[:]:
            if head_rect.colliderect(f.get_rect()):
                # yum, yum
                # remove the food and add a segment
                food_items.remove(f)

                last_piece = self._head
                for last_piece in self._segments:
                    pass

                x = last_piece['pos'][0] 
                y = last_piece['pos'][1] + 30
                self._add_segment([x,y])

        
if __name__ == "__main__":
    # Or you could run unit tests...
    pass
