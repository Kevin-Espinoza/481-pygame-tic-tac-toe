import sys, pygame
from constants import *
from game import TicTacToe


# Main
if __name__ == '__main__':
    
    # GAME OBJECT
    tictactoe = TicTacToe()
    ai = tictactoe.computer

    # MAIN LOOP
    while True:
        for event in pygame.event.get():
            # EXIT WINDOW EVENT LISTENER
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # MOUSE CLICK EVENT LISTENER TO PLAY GAME
            if event.type == pygame.MOUSEBUTTONDOWN:
                # CONVERT FROM COORDINATES TO CELL INDEX
                CELL_location = event.pos
                row = CELL_location[1] // CELL_SIZE
                column = CELL_location[0] // CELL_SIZE

                # PLACE PLAYER MARKER AT LOCATION WITHIN BOARD ARARY.
                # AND DRAW PLAYER MARKER TO CANVAS.
                if tictactoe.game_board.empty(row, column) and tictactoe.running:
                    tictactoe.draw_and_save_move(row, column)
                    if tictactoe.game_over():
                        tictactoe.running = False

            # PRESS R TO RESTART GAME
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    tictactoe.reset_game()
                    tictactoe.game_board = tictactoe.game_board
                    ai = tictactoe.computer

        if tictactoe.player == ai.player and tictactoe.running:
            pygame.display.update()
            row, column = ai.evaluate(tictactoe.game_board)
            tictactoe.draw_and_save_move(row, column)

            if tictactoe.game_over():
                        tictactoe.running = False

        pygame.display.update()

