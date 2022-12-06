#######################################
### AVOIDANCE TIC-TAC-TOE w/ Pygame ###
###  ------------------------------ ###
### Objective is to avoid getting 3 ###
### in a row against competitive AI ###
#######################################
import sys
import pygame as pg
from random import randint
from constants import *


# TicTacToe class
class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.img_grid = self.get_scaled_image(path = 'assets/grid.png', res=[WINDOW_SIZE] * 2)
        self.img_o = self.get_scaled_image(path = 'assets/o.png', res=[CELL_SIZE] * 2)
        self.img_x = self.get_scaled_image(path = 'assets/x.png', res=[CELL_SIZE] * 2)
        
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]

        self.player = randint(0, 1) # randomly determines whether player is X or O
                                    # 'X' = 1
                                    # 'O' = 0
        
        self.line_indices_array = [ [(0, 0), (0, 1), (0, 2)],
                                    [(1, 0), (1, 1), (1, 2)],
                                    [(2, 0), (2, 1), (2, 2)],
                                    [(0, 0), (1, 0), (2, 0)],
                                    [(0, 1), (1, 1), (2, 1)],
                                    [(0, 2), (1, 2), (2, 2)],
                                    [(0, 0), (1, 1), (2, 2)],
                                    [(0, 2), (1, 1), (2, 0)]]
        self.loser = None
        self.game_steps = 0
        self.font = pg.font.SysFont('Verdana', CELL_SIZE // 4, True)

    def check_loser(self):
            for line_indices in self.line_indices_array:
                sum_line = sum([self.game_array[i][j] for i, j in line_indices])
                if sum_line in {0, 3}:
                    self.loser = 'XO'[sum_line == 0]
                    self.loser_line = [vector2(line_indices[0][::-1]) * CELL_SIZE + CENTER,
                                       vector2(line_indices[2][::-1]) * CELL_SIZE + CENTER]

    # main game functionality
    def run_game_process(self):
        current_cell = vector2(pg.mouse.get_pos()) // CELL_SIZE
        col, row = map(int, current_cell)
        left_click = pg.mouse.get_pressed()[0]

        if left_click and self.game_array[row][col] == INF and not self.loser:
            self.game_array[row][col] = self.player
            self.player = not self.player
            self.game_steps += 1
            self.check_loser()

    # displays game array
    def draw_objects(self):
        for y, row in enumerate(self.game_array):
            for x, obj in enumerate(row):
                # if cell is INF then it is blank
                if obj != INF: 
                    self.game.screen.blit(self.img_x if obj else self.img_o, vector2(x, y) * CELL_SIZE)

    def draw_loser(self):
        if self.loser:
            pg.draw.line(self.game.screen, 'red', *self.loser_line, CELL_SIZE // 8)
            label = self.font.render(f'Player "{self.loser}" loses!', True, 'white', 'purple')
            self.game.screen.blit(label, (WINDOW_SIZE // 2 - label.get_width() // 2, WINDOW_SIZE // 4))
            

    # draw assets at given location (origin point (0,0))
    def draw(self):
        self.game.screen.blit(self.img_grid, (0,0))
        # self.game.screen.blit(self.img_o, (0,0))
        # self.game.screen.blit(self.img_x, (300,300))
        self.draw_objects()
        self.draw_loser()

    # load and scale images
    @staticmethod
    def get_scaled_image(path,res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)

    def print_caption(self):
        pg.display.set_caption(f'Player "{"OX"[self.player]}" turn!')
        if self.loser:
            pg.display.set_caption(f'Player "{self.loser}" loses! Press Space to Restart')
        elif self.game_steps == 9:
            pg.display.set_caption(f'Game Over! Press Space to Restart')

    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()

# game class
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WINDOW_SIZE] * 2)
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
            self.tic_tac_toe.run()  # start game
            self.check_events()     # event checker
            pg.display.update()     # render surface
            self.clock.tick(60)     # refresh rate

# class AI:

if __name__ == '__main__':
    game = Game()
    game.run()