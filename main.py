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

# TicTacToe class
class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.img_grid = self.get_scaled_image(path='assets/grid.png', res=[window_size] * 2)
        self.img_o = self.get_scaled_image(path='assets/o.png', res=[cell_size] * 2)
        self.img_x = self.get_scaled_image(path='assets/x.png', res=[cell_size] * 2)
        pass
    # draw assets at given location (origin point (0,0))
    def draw(self):
        self.game.screen.blit(self.img_grid, (0,0))
        #self.game.screen.blit(self.img_o, (0,0))
        #self.game.screen.blit(self.img_x, (300,300))

    # load and scale images
    @staticmethod
    def get_scaled_image(path,res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img,res)
    def run(self):
        self.draw()
        pass

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
                pg.quite()
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