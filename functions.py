import numpy as np

# Board Size
ROW_COUNT = 6
COL_COUNT = 7


def create_board():
    return np.zeros((ROW_COUNT,COL_COUNT), dtype=int)


def update_board(board, col, piece):
    row_init = ROW_COUNT-1
    while row_init>=0:
        if board[row_init, col] == 0:
            board[row_init, col] = piece
            return board
        row_init-=1
    return board


def is_valid_column(board, col):
    if col <= (COL_COUNT-1) and col >= 0:
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
