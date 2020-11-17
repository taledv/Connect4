import numpy as np
import pygame
from functions import create_board, is_valid_column, update_board, check_for_win, draw_board, winning_indices, draw_end_board, draw_intro_screen
from functions import intro_screen, p_vs_p, p_vs_ai
import sys

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

Choise = intro_screen(screen, board)

myfont = pygame.font.SysFont('monospace', 75)
turn = np.random.randint(2)

game_over = False

if Choise == Player:
    p_vs_p(screen, board, turn, game_over, myfont)
else:
    p_vs_ai(screen, board, turn, game_over, myfont)


