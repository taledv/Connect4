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
RED = (200, 0, 0)
RED_WIN = (139, 0, 0)
YELLOW_WIN = (255, 127, 80)
WHITE = (255, 255, 255)


def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT), dtype=int)


def draw_intro_screen(screen):
    for row in range(ROW_COUNT+1):
        for col in range(COL_COUNT):
            pygame.draw.rect(screen, WHITE, (col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if row == 3 and col == 2:
                pygame.draw.rect(screen, RED, (col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if row == 3 and col == 5:
                pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE))

    myfont = pygame.font.SysFont('monospace', 25)
    label = myfont.render('AI', 1, RED)
    screen.blit(label, (240, 270))
    label = myfont.render('PVsP', 1, BLUE)
    screen.blit(label, (520, 270))

    myfont = pygame.font.SysFont('monospace', 60)
    label = myfont.render('Welcome to Connect4 (:', 1, BLACK)
    screen.blit(label, (10, 10))
    pygame.display.update()  # Update the graphics


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
                # print(row, col)
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


def winning_indices(board, piece):
    # Horizontal Check
    for row in range(ROW_COUNT):
        for col in range(COL_COUNT-3):
            if all(board[row, col:col+4] == piece):
                return np.array([[row, col], [row, col+1], [row, col+2], [row, col+3]])

    # Vertical Check
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT-3):
            if all(board[row:row+4, col] == piece):
                return np.array([[row, col], [row+1, col], [row+2, col], [row+3, col]])

    # negative diagonals
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT-3):
            if (board[row, col] == piece) and (board[row+1, col+1] == piece) and (board[row+2, col+2] == piece) and (board[row+3, col+3] == piece):
                return np.array([[row, col], [row+1, col+1], [row+2, col+2], [row+3, col+3]])

    # positive diagonals
    for row in range(ROW_COUNT-3):
        for col in range(COL_COUNT-1, 2, -1):
            if (board[row, col] == piece) and (board[row+1, col-1] == piece) and (board[row+2, col-2] == piece) and (board[row+3, col-3] == piece):
                return np.array([[row, col], [row+1, col-1], [row+2, col-2], [row+3, col-3]])


def draw_end_board(board, screen, winning_indices):

    draw_board(board, screen)

    for i in range(winning_indices.shape[0]):
        if board[winning_indices[i, 0], winning_indices[i, 1]] == 1:
            pygame.draw.circle(screen, RED_WIN, ((winning_indices[i, 1]+0.5)*SQUARESIZE, (winning_indices[i, 0]+1.5)*SQUARESIZE), SQUARESIZE/2-3)
        else:
            pygame.draw.circle(screen, YELLOW_WIN, ((winning_indices[i, 1]+0.5)*SQUARESIZE, (winning_indices[i, 0]+1.5)*SQUARESIZE), SQUARESIZE/2-3)
    pygame.display.update()  # Update the graphics