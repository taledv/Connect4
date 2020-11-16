import numpy as np
import pygame
# Board Size
ROW_COUNT = 6
COL_COUNT = 7

SQUARESIZE = 100
width = COL_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE
size = (width, height)

BLUE = (0, 0, 200)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (200, 0 , 0)


def create_board():
    return np.zeros((ROW_COUNT,COL_COUNT), dtype=int)


def draw_board(board, screen):
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT):
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, (row+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[row, col] == 0:
                pygame.draw.circle(screen, BLACK, ((col+0.5)*SQUARESIZE, (row+1.5)*SQUARESIZE), SQUARESIZE/2-3)
            elif board[row, col] == 1:
                pygame.draw.circle(screen, RED, ((col+0.5)*SQUARESIZE, (row+1.5)*SQUARESIZE), SQUARESIZE/2-3)
            else:
                pygame.draw.circle(screen, YELLOW, ((col+0.5)*SQUARESIZE, (row+1.5) * SQUARESIZE), SQUARESIZE/2 - 3)
    pygame.display.update()  # Update the graphics


def update_board(board, col, piece):
    row_init = ROW_COUNT-1
    while row_init>=0:
        if board[row_init, col] == 0:
            board[row_init, col] = piece
            return board
        row_init -= 1
    return board


def is_valid_column(board, col):
    if (col <= (COL_COUNT-1)) and (col >= 0):
        if board[0, col] == 0:
            return True
    return False


def check_for_win(board, piece):
    # Horizontal Check
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT-3):
            if all(board[row, col:col+4] == piece):
                return True
    # Vertical Check
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT-3):
            if all(board[row:row+4, col] == piece):
                return True
    # negative diagonals
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT-3):
            if (board[row, col] == piece) and (board[row+1, col+1] == piece) and (board[row+2, col+2] == piece) and (board[row+3, col+3] == piece):
                return True
    # positive diagonals
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT-1, 2, -1):
            if (board[row, col] == piece) and (board[row+1, col-1] == piece) and (board[row+2, col-2] == piece) and (board[row+3, col-3] == piece):
                return True
    return False
