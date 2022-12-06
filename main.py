#######################################
### AVOIDANCE TIC-TAC-TOE w/ Pygame ###
###  ------------------------------ ###
### Objective is to avoid getting 3 ###
### in a row against competitive AI ###
#######################################
import sys
import pygame as pg
from random import randint

window_size = 900 # size of game window (900px)
cell_size = window_size // 3 # size of individual cell (300px)
INF = float('inf') # variable to hold infinity
vec2 = pg.math.Vector2

# TicTacToe class
class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.img_grid = self.get_scaled_image(path='assets/grid.png', res=[window_size] * 2)
        self.img_o = self.get_scaled_image(path='assets/o.png', res=[cell_size] * 2)
        self.img_x = self.get_scaled_image(path='assets/x.png', res=[cell_size] * 2)
        
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]

        self.player = randint(0, 1) # randomly determines whether player is X or O

    # main game functionality
    def run_game_process(self):
        current_cell = vec2(pg.mouse.get_pos()) // cell_size
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]

        if left_click and self.game_array[row][col] == INF:
            self.game_array[row][col] = self.player
            self.player = not self.player

    # displays game array
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                # if cell is INF then it is blank
                if obj != INF: 
                    self.game.screen.blit(self.img_x if obj else self.img_o, vec2(x, y) * cell_size)

    # draw assets at given location (origin point (0,0))
    def draw(self):
        self.game.screen.blit(self.img_grid, (0,0))
        # self.game.screen.blit(self.img_o, (0,0))
        # self.game.screen.blit(self.img_x, (300,300))
        self.draw_objects()

    # load and scale images
    @staticmethod
    def get_scaled_image(path,res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img,res)

    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')

    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()

# game class
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([window_size] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        # exit window event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    # game loop
    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events() # event checker
            pg.display.update() # render surface
            self.clock.tick(60) # refresh rate

if __name__ == '__main__':
    game = Game()
    game.run()