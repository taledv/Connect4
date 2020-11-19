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

Player = 1
AI = 2

while 1:
    board = create_board()
    turn = np.random.randint(2)  # Random initial player

    pygame.init()  # Init pygame
    pygame.display.set_mode(size)  # Set window size
    screen = pygame.display.set_mode(size)  # Init screen (surface)

    game_mode, ai_lvl = intro_screen(screen, board)

    if game_mode == Player:
        p_vs_p(screen, board, turn)
    else:
        p_vs_ai(screen, board, turn, ai_lvl)
