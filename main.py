#######################################
### AVOIDANCE TIC-TAC-TOE w/ Pygame ###
###  ------------------------------ ###
### Objective is to avoid getting 3 ###
### in a row against competitive AI ###
#######################################
from functools import reduce
import sys
import pygame as pg
from random import randint, choice
from constants import *
import numpy as np
import copy


class AI:
    def __init__(self, player=0):
        # The AI will play as 'O' in the game
        self.player = player 

    def rndm(self):
        pass
        # empty_squares = 

# TicTacToe class
class TicTacToe:
    def __init__(self, game):
        self.ai = AI()
        self.game = game 
        self.img_grid = self.get_scaled_image(path = 'assets/grid.png', res=[WINDOW_SIZE] * 2)
        self.img_o = self.get_scaled_image(path = 'assets/o.png', res=[CELL_SIZE] * 2)
        self.img_x = self.get_scaled_image(path = 'assets/x.png', res=[CELL_SIZE] * 2)
        
        self.game_array = [[INF, INF, INF],
                           [INF, INF, INF],
                           [INF, INF, INF]]

        self.player = 1 # player is X, AI will be O
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

        # Possible moves will be passed to AI and will be updated to remove cells the player places their X on
        self.possible_moves = [ (0, 0), (0, 1), (0, 2),
                                (1, 0), (1, 1), (1, 2),
                                (2, 0), (2, 1), (2, 2) ]

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

            # Remove the move that the player took from possible_moves
            self.possible_moves.remove((row, col))

            # Switch current player to AI if not last move
            if len(self.possible_moves) > 1:
                self.player = not self.player
                # Call AI to find a cell and return the value to populate in game
                ai_move = self.ai.minimax(self.possible_moves, False, self.game_array)
                self.game_array[ai_move[0]][ai_move[1]] = self.player
                # Remove the move AI took from possible_moves
                self.possible_moves.remove((ai_move[0], ai_move[1]))
                # Switch current player to Human Player
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


class AI:
    def __init__(self, player=0):
        self.player = player

    # Get the list of possible moves and return one possible move
    def minimax(self, empty_squares, maximizing, game_board):

        if maximizing:
            maximum_eval = -10
            best_move = None
            empty_sqrs = empty_squares
            for x in empty_sqrs:
                temp_board = copy.deepcopy(game_board)
                # temp_board.mark_sqr(row, col, 1)

                # temp_board = temp_board[x[0]],[x[1]]
                temp_board[int(i),int(j)] = self.player
                self.player=0

                # Remove the move AI took from possible_moves
                empty_sqrs.remove(list(x))

                eval = self.minimax(temp_board, False, temp_board)[0]
                if eval > maximum_eval:
                    maximum_eval = eval
                    best_move = (list(x))
            return minimum_eval, best_move

        elif not maximizing:
            minimum_eval = 10
            best_move = None
            empty_sqrs = empty_squares

            print('EMPTY SQUARES: ', empty_sqrs)

            for x in empty_sqrs:
                temp_board = copy.deepcopy(game_board)
                # temp_board.mark_sqr(row, col, self.player)

                i, j = x[0], x[1]

                print('TEMP BOARD: ', type(i),j)
                temp_board[int(i),int(j)] = self.player
                self.player=1
                # Remove the move AI took from possible_moves
                empty_sqrs.remove((list(x)))

                eval = self.minimax(temp_board, True, temp_board)[0]
                if eval < minimum_eval:
                    minimum_eval = eval
                    best_move = (list(x))
        return minimum_eval, best_move

    def eval(self, empty_squares):
        move = self.minimax(empty_squares, False)
        return move


    # TODO: DELETE AFTER
    def randm(self, empty_squares):
        # TODO: Use empty_squares to find legal moves
        print('GAME BOARD: ', empty_squares)
        # Generate random move based on num of available moves and return that 
        print('AI RAND: ', randint(0, len(empty_squares)))
        num = randint(0, len(empty_squares)-1)
        print('CHOSEN: ', list(empty_squares[num]))
        game_array = list(empty_squares[num])

        return game_array




# game class
class Game:
    def __init__(self):
        pg.init()
        self.ai = AI()
        self.screen = pg.display.set_mode([WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        # exit window event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            # Press space to reset the gameboard, can be done at any time
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.new_game()

    # Reset the gameboard
    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    # game loop
    def run(self):
        while True:
            self.tic_tac_toe.run()  # start game
            self.check_events()     # event checker
            pg.display.update()     # render surface
            self.clock.tick(60)     # refresh rate

if __name__ == '__main__':
    game = Game()
    game.run()