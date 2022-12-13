import copy
from constants import *

# AI BLUEPRINT
class AI:
    def __init__(self, player=2):
        self.player = player

    def minimax(self, board, maximize):
        # TERMINAL CASE CHECK
        case = board.loss()
        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        elif board.full_board():
            return 0, None

        # MINIMAX ALGORITHM
        if maximize:
            maximize_evaluate = -2
            best_move = None
            empty_cells = board.get_empty()
            for (row, column) in empty_cells:
                temporary_board = copy.deepcopy(board)
                temporary_board.place_marker(row, column, self.player)
                evaluate = self.minimax(temporary_board, False)[0]
                if evaluate > maximize_evaluate:
                    maximize_evaluate = evaluate
                    best_move = (row, column)
            return maximize_evaluate, best_move

        elif not maximize:
            minimize_evaluate = 2
            best_move = None
            empty_cells = board.get_empty()
            for (row, column) in empty_cells:
                temporary_board = copy.deepcopy(board)
                temporary_board.place_marker(row, column, 1)
                evaluate = self.minimax(temporary_board, True)[0]
                if evaluate < minimize_evaluate:
                    minimize_evaluate = evaluate
                    best_move = (row, column)
            return minimize_evaluate, best_move

    def evaluate(self, board):
        if self.player:
            evaluate, move = self.minimax(board, True)
        return move
