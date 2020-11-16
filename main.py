import numpy as np
import pygame
from functions import create_board, is_valid_column, update_board, check_for_win

# Board Size
ROW_COUNT = 6
COL_COUNT = 7

board = create_board()
turn = 0

# SQUARESIZE = 100
# width = COL_COUNT*SQUARESIZE
# height = (ROW_COUNT+1)*SQUARESIZE
# size = (width, height)
#
# pygame.init()
# pygame.display.set_mode(size)

# screen = pygame.display.set_mode(size)

while 1:
    if all(board[0, :] > 0):
        print('No one won!, It is a TIE!')
        break
    if turn == 0:
        # Player 1
        col = int(input('Player 1: Enter a valid column number (1-7):'))

        if is_valid_column(board, col-1):
            board = update_board(board, col-1, turn+1)
        else:
            while not is_valid_column(board, col-1):
                col = int(input('Player 1: Please pick a valid column:'))
            board = update_board(board, col-1, turn+1)

        print(board)
        if check_for_win(board, turn+1):
            print('Player 1 WON !')
            break
    else:
        # Player 2
        col = int(input('Player 2: Enter a valid column number (1-7):'))

        if is_valid_column(board, col-1):
            board = update_board(board, col-1, turn+1)
        else:
            while not is_valid_column(board, col-1):
                col = int(input('Player 2: Please pick a valid column:'))
            board = update_board(board, col-1, turn+1)

        print(board)
        if check_for_win(board, turn+1):
            print('Player 2 WON !')
            break
    turn = 1 - turn  # Change turn
