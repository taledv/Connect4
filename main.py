import numpy as np
import pygame
from functions import create_board, intro_screen, p_vs_p, p_vs_ai

# Board Size
ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 100

width = COL_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE
size = (width, height)

board = create_board()

Player = 1
AI = 2

pygame.init()  # Init pygame
pygame.display.set_mode(size)  # Set window size
screen = pygame.display.set_mode(size)  # Init screen (surface)

# game_mode = intro_screen(screen, board)

myfont = pygame.font.SysFont('monospace', 75)
turn = np.random.randint(2)
game_over = False

p_vs_ai(screen, board, turn, game_over, myfont)


#
# if game_mode == Player:
#     p_vs_p(screen, board, turn, game_over, myfont)
# else:
#     p_vs_ai(screen, board, turn, game_over, myfont)


