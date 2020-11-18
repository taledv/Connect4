import numpy as np
import pygame
import sys
import math

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
YELLOW_WIN = (255, 243, 128)
WHITE = (255, 255, 255)
Player = 1
AI = 2


def draw_intro_screen(screen):
    for row in range(ROW_COUNT+1):
        for col in range(COL_COUNT):
            pygame.draw.rect(screen, YELLOW_WIN, (col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE))

    pygame.draw.rect(screen, RED, (150, 350, SQUARESIZE, SQUARESIZE))  # AI BUTTON
    pygame.draw.rect(screen, BLUE, (450, 350, SQUARESIZE, SQUARESIZE))  # PVP BUTTON

    myfont = pygame.font.SysFont('monospace', 25)
    label = myfont.render('AI', 1, RED)
    screen.blit(label, (185, 320))
    label = myfont.render('PVsP', 1, BLUE)
    screen.blit(label, (475, 320))

    myfont = pygame.font.SysFont('monospace', 50)
    label = myfont.render('Welcome to Connect4 !', 1, BLACK)
    screen.blit(label, (30, 30))

    myfont = pygame.font.SysFont('monospace', 40)
    label = myfont.render('Choose a game mode:', 1, BLACK)
    screen.blit(label, (150, 200))

    pygame.display.update()  # Update the graphics


def intro_screen(screen, board):

    draw_intro_screen(screen)
    pygame.display.update()  # Update the graphics

    intro_screen = True
    while intro_screen:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > 150 and event.pos[0] < 250 and event.pos[1] > 350 and event.pos[1] < 450:
                    Choise = AI
                elif event.pos[0] > 450 and event.pos[0] < 550 and event.pos[1] > 350 and event.pos[1] < 450:
                    Choise = Player
                else:
                    continue
                for col in range(COL_COUNT):
                    pygame.draw.rect(screen, BLACK, (col * SQUARESIZE, 0, SQUARESIZE, SQUARESIZE))
                intro_screen = False

    draw_board(board, screen)  # Draw the board with recs and black circles
    pygame.display.update()  # Update the graphics
    return Choise


def p_vs_p(screen, board, turn, game_over, myfont):
    while not game_over:
        if all(board[0, :] > 0):
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            label = myfont.render('It is a TIE', 1, WHITE)
            screen.blit(label, (40, 10))
            game_over = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                if turn == 0:
                    pygame.draw.circle(screen, RED, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                else:
                    pygame.draw.circle(screen, YELLOW, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    # Player 1
                    col = int(event.pos[0] / SQUARESIZE) + 1  # Between 1-7

                    if is_valid_column(board, col - 1):
                        board = update_board(board, col - 1, turn + 1)
                        if check_for_win(board, turn + 1):
                            win_indices = winning_indices(board, turn + 1)

                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                            label = myfont.render('Player 1 WINS', 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True
                        turn = 1 - turn
                else:
                    # Player 2
                    col = int(event.pos[0] / SQUARESIZE) + 1  # Between 1-7

                    if is_valid_column(board, col - 1):
                        board = update_board(board, col - 1, turn + 1)
                        if check_for_win(board, turn + 1):
                            win_indices = winning_indices(board, turn + 1)

                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                            label = myfont.render('Player 2 WINS', 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True
                        turn = 1-turn

                draw_board(board, screen)

                if game_over:
                    draw_end_board(board, screen, win_indices)
                    pygame.display.update()
                    pygame.time.delay(2500)

                # Immediately change color of the piece. don't wait for motion of the mouse
                if not game_over:
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                    else:
                        pygame.draw.circle(screen, YELLOW, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                    pygame.display.update()


def p_vs_ai(screen, board, turn, game_over, myfont):
    while not game_over:
        draw_board(board, screen)
        if all(board[0, :] > 0):
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            label = myfont.render('It is a TIE', 1, WHITE)
            screen.blit(label, (40, 10))
            game_over = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                if turn == 0:
                    pygame.draw.circle(screen, RED, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                else:
                    pygame.draw.circle(screen, YELLOW, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    # Human player
                    col = int(event.pos[0] / SQUARESIZE) + 1  # Between 1-7
                    if is_valid_column(board, col - 1):
                        board = update_board(board, col - 1, turn + 1)
                        if check_for_win(board, turn + 1):
                            win_indices = winning_indices(board, turn + 1)

                            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                            label = myfont.render('You Won!', 1, RED)
                            screen.blit(label, (180, 10))
                            game_over = True
                        turn = 1 - turn
                        draw_board(board, screen)
        # AI
        if turn == 1 and not game_over:

            # Random AI - Beginner
            # col = np.random.randint(1, 8)  # Between 1-7
            # Better AI - Advanced
            col = pick_best_col(board)
            # Best AI - Expert
            # col = minimax(board, depth=3, Maximizier=AI)

            pygame.time.delay(400)
            if is_valid_column(board, col - 1):
                board = update_board(board, col - 1, turn + 1)
                if check_for_win(board, turn + 1):
                    win_indices = winning_indices(board, turn + 1)

                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    label = myfont.render('AI Won!', 1, YELLOW)
                    screen.blit(label, (180, 10))
                    game_over = True
                turn = 1 - turn
                draw_board(board, screen)

        if game_over:
            draw_end_board(board, screen, win_indices)
            pygame.display.update()
            pygame.time.delay(3000)


def minimax(board, depth, Maximizier):
    val_cols = valid_cols(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_for_win(board, AI):
                return 1000000
            elif check_for_win(board, Player):
                return -1000000
            else:
                return 0  # Game over
        else:  # depth is zero
            score_position(board)
    if Maximizier:
        value = -math.inf
        for col in val_cols:
            board_next = board.copy()
            board_next = update_board(board_next, col, AI)
            new_score = max(value, minimax(board_next, depth-1, False))
            return new_score
    else:  # We are the minimizer player
        value = math.inf
        for col in val_cols:
            board_next = board.copy()
            board_next = update_board(board_next, col, Player)
            new_score = min(value, minimax(board_next, depth - 1, True))
            return new_score


def is_terminal_node(board):
    return check_for_win(board, AI) or check_for_win(board, Player) or len(valid_cols(board)) == 0


def pick_best_col(board):
    best_score = -1000
    best_col = np.random.randint(1, 8)

    for col in valid_cols(board):
        next_state_board = board.copy()
        next_state_board = update_board(next_state_board, col, AI)
        score = score_position(next_state_board)
        print((col, score))
        if score > best_score:
            best_score = score
            best_col = col
    return best_col+1  # convert 0-6 to 1-7


def score_position(next_state_board):
    score = 0

    # Gives extra points for center column
    cen_col_list = [int(i) for i in list(next_state_board[:, COL_COUNT//2])]
    center_count = cen_col_list.count(AI)
    score += 6 * center_count

    # Horizontal
    for row in range(ROW_COUNT):
        row_list = [int(i) for i in list(next_state_board[row, :])]
        for col in range(COL_COUNT-3):
            window = row_list[col:col+4]
            score += evaluate_window(window)

    # Vertical
    for col in range(COL_COUNT):
        col_list = [int(i) for i in list(next_state_board[:, col])]
        for row in range(ROW_COUNT-3):
            window = col_list[row:row+4]
            score += evaluate_window(window)

    # Negative diagonal
    for row in range(ROW_COUNT - 3):
        for col in range(COL_COUNT - 3):
            window = [next_state_board[row, col], next_state_board[row + 1, col + 1],
                      next_state_board[row + 2, col + 2], next_state_board[row + 3, col + 3]]
            score += evaluate_window(window)

    # Positive diagonal
    for row in range(ROW_COUNT - 3):
        for col in range(COL_COUNT-1, 2, -1):
            window = [next_state_board[row, col], next_state_board[row + 1, col - 1],
                      next_state_board[row + 2, col - 2], next_state_board[row + 3, col - 3]]
            score += evaluate_window(window)
    return score


def evaluate_window(window):
    score = 0
    if window.count(AI) == 4:
        score += 100
    elif window.count(AI) == 3 and window.count(0) == 1:
        score += 10
    elif window.count(AI) == 2 and window.count(0) == 2:
        score += 5
    elif window.count(Player) == 2 and window.count(0) == 2:
        score -= 8
    elif window.count(Player) == 3 and window.count(0) == 1:
        score -= 80
    return score


def create_board():
    return np.zeros((ROW_COUNT, COL_COUNT), dtype=int)


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
    while row_init >= 0:
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


def valid_cols(board):
    val_cols = []
    for col in range(COL_COUNT):
        if is_valid_column(board, col):
            val_cols.append(col)
    return val_cols


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