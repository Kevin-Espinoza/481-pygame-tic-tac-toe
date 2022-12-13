import numpy as np
from constants import *

# GAME BOARD BLUEPRINT
class Board:
    def __init__(self):
        self.cells = np.zeros((ROWS,COLUMNS))
        self.empty_cells = self.cells
        self.not_empty_cells = 0

    def loss(self, draw_loss=False):
        # CHECK VERTICAL LOSS
        for column in range(COLUMNS):
            if self.cells[0][column] == self.cells[1][column] == self.cells[2][column] != 0:
                # DRAW LOSS LINE
                if draw_loss:
                    start_position = (column * CELL_SIZE + CELL_SIZE // 2, OFFSET2)
                    end_position = (column * CELL_SIZE + CELL_SIZE // 2, HEIGHT - OFFSET2)
                    pygame.draw.line(canvas, LOSS_COLOR, start_position, end_position, LOSS_WIDTH)
                    self.loss_bannar()
                return self.cells[0][column]
        # CHECK HORIZONTAL LOSS
        for row in range(ROWS):
            if self.cells[row][0] == self.cells[row][1] == self.cells[row][2] != 0:
                # DRAW LOSS LINE
                if draw_loss:
                    start_position = (OFFSET2, row * CELL_SIZE + CELL_SIZE // 2)
                    end_position = (WIDTH - OFFSET2, row * CELL_SIZE + CELL_SIZE // 2)
                    pygame.draw.line(canvas, LOSS_COLOR, start_position, end_position, LOSS_WIDTH)
                return self.cells[row][0]
        # CHECK DIAGONAL LOSS
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] != 0:
            # DRAW LOSS LINE
            if draw_loss:
                start_position = (OFFSET2, OFFSET2)
                end_position = (WIDTH - OFFSET2, HEIGHT - OFFSET2)
                pygame.draw.line(canvas, LOSS_COLOR, start_position, end_position, LOSS_WIDTH)
            return self.cells[1][1]
        if self.cells[2][0] == self.cells[1][1] == self.cells[0][2] != 0:
            # DRAW LOSS LINE
            if draw_loss:
                start_position = (OFFSET2, HEIGHT - OFFSET2)
                end_position = (WIDTH - OFFSET2, OFFSET2)
                pygame.draw.line(canvas, LOSS_COLOR, start_position, end_position, LOSS_WIDTH)
            return self.cells[1][1]
        return 0

    def place_marker(self, row, column, player):
        self.cells[row][column] = player
        self.not_empty_cells += 1

    # Checks if current cell is empty
    def empty(self, row, column):
        return self.cells[row][column] == 0

    # Gets all empty cells
    def get_empty(self):
        empty_cells = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.empty(row, column):
                    empty_cells.append((row,column))
        return empty_cells

    # Return true if all cells have been filled
    def full_board(self):
        return self.not_empty_cells == 9
