import numpy as np
import pygame
from functions import create_board, is_valid_column, update_board, check_for_win, draw_board, winning_indices, draw_end_board
import sys

# Board Size
ROW_COUNT = 6
COL_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

board = create_board()
turn = 0

game_over = False

SQUARESIZE = 100
width = COL_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE
size = (width, height)

pygame.init()  # Init pygame
pygame.display.set_mode(size)  # Set window size

screen = pygame.display.set_mode(size)  # Init screen (surface)
draw_board(board, screen)  # Draw the board with recs and black circles
pygame.display.update()  # Update the graphics

myfont = pygame.font.SysFont('monospace', 75)

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
                pygame.draw.circle(screen, RED, (event.pos[0], SQUARESIZE/2), SQUARESIZE/2-3)
            else:
                pygame.draw.circle(screen, YELLOW, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                # Player 1
                col = int(event.pos[0]/SQUARESIZE)+1  # Between 1-7

                if is_valid_column(board, col-1):
                    board = update_board(board, col-1, turn+1)
                else:
                    turn = 1-turn  # don't change turns if invalid column

                if check_for_win(board, turn+1):
                    win_indices = winning_indices(board, turn+1)

                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    label = myfont.render('Player 1 WINS', 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True
            else:
                # Player 2
                col = int(event.pos[0]/SQUARESIZE)+1  # Between 1-7

                if is_valid_column(board, col-1):
                    board = update_board(board, col-1, turn+1)
                else:
                    turn = 1 - turn  # don't change turns if invalid column

                if check_for_win(board, turn+1):
                    win_indices = winning_indices(board, turn+1)

                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    label = myfont.render('Player 2 WINS', 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

            draw_board(board, screen)

            if game_over:
                draw_end_board(board, screen, win_indices)
                pygame.display.update()
                pygame.time.delay(2500)

            turn = 1 - turn  # Change turn
            # Immediately change color of the piece. don't wait for motion of the mouse
            if not game_over:
                if turn == 0:
                    pygame.draw.circle(screen, RED, (event.pos[0], SQUARESIZE/2), SQUARESIZE/2-3)
                else:
                    pygame.draw.circle(screen, YELLOW, (event.pos[0], SQUARESIZE / 2), SQUARESIZE / 2 - 3)
                pygame.display.update()
