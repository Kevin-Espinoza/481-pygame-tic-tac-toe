import pygame
from constants import *
from board import Board
from ai import AI


# GAME BLUEPRINT
class TicTacToe:
    def __init__(self):
        self.game_board = Board()
        self.computer = AI()
        self.player = 1
        self.running = True
        self.draw_board()

    def draw_and_save_move(self, row, column):
        # DRAW PLAYER MARKER AND CHANGE PLAYER TURN
        self.game_board.place_marker(row, column, self.player)
        self.draw_marker(row, column)
        self.change_turn()

    def draw_board(self):
        # DRAW LINES (GAME BOARD)
        canvas.fill(BACKGROUND_COLOR)
        pygame.draw.line(canvas, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(canvas, LINE_COLOR, (WIDTH - CELL_SIZE, 0), (WIDTH - CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(canvas, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(canvas, LINE_COLOR, (0, HEIGHT - CELL_SIZE), (WIDTH, HEIGHT - CELL_SIZE), LINE_WIDTH)

    def draw_marker(self, row, column):
        # DRAW 'X' OR 'O' TO CANVAS
        if self.player == 1:
            start_location = (column * CELL_SIZE + OFFSET, row * CELL_SIZE + OFFSET)
            end_location = (column * CELL_SIZE + CELL_SIZE - OFFSET, row * CELL_SIZE + CELL_SIZE - OFFSET)
            pygame.draw.line(canvas, X_COLOR, start_location, end_location, X_WIDTH)
            start_location = (column * CELL_SIZE + OFFSET, row * CELL_SIZE + CELL_SIZE - OFFSET)
            end_location = (column * CELL_SIZE + CELL_SIZE - OFFSET, row * CELL_SIZE + OFFSET)
            pygame.draw.line(canvas, X_COLOR, start_location, end_location, X_WIDTH)
        elif self.player == 2:
            center = (column * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.circle(canvas, O_COLOR, center, O_RADIUS, O_WIDTH)

    def game_over(self):
        # GAME OVER DETECTED
        return self.game_board.loss(draw_loss=True) !=0 or self.game_board.full_board()

    def change_turn(self):
        # CHANGE PLAYER TURN
        self.player = self.player % 2 + 1

    def reset_game(self):
        # GAME RESET DETECTED
        self.__init__()