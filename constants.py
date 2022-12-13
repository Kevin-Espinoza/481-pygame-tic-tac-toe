import pygame

# GLOBAL CONSTANTS
WIDTH = 600
HEIGHT = 600
ROWS, COLUMNS = 3, 3
LINE_WIDTH = 5
LOSS_WIDTH = 10
O_WIDTH = 30
CELL_SIZE = WIDTH // COLUMNS
O_RADIUS = CELL_SIZE // 2.5
BACKGROUND_COLOR = (250, 249, 246)
LINE_COLOR= (0, 0, 0)
O_COLOR= (39, 174, 96)
X_COLOR= (41, 128, 185)
X_WIDTH = 45
OFFSET = 33
OFFSET2 = 20
LOSS_COLOR= (220, 20, 60)

# PYGAME SETTINGS
pygame.init()
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Avoidance TicTacToe -- Press R to restart game')
canvas.fill(BACKGROUND_COLOR)