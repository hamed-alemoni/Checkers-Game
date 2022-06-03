import pygame
from .constant import WHITE, BLACK, RED, ROWS, COLUMNS, SQUARE_SIZE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.selected_peace = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, window):
        
        window.fill(BLACK)

        for row in range(ROWS):
            for column in range(row % 2 , COLUMNS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                #                                  position x            position y         size of edges             


    def create_board(self):
        for row in range(ROWS):

            self.board.append([])

            for column in range(COLUMNS):
                # determine which square we should put piece
                if column % 2 == ((row + 1) % 2):
                    # determine the square should fill with white piece, red one or it should be empty
                    if row < 3:
                        self.board[row].append(Piece(row, column, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)  

    # first draw squares then draw each piece onto square
    def draw_window(self, window):

        self.draw_squares(window)

        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw_piece(window)

    def get_piece(self, row, column):
        
        return self.board[row][column]
    

    def move(self, piece, row, column):
        # swap in board list
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], self.board[piece.row][piece.column]

        piece.move_piece(row, column)

        # piece make a king
        if row == ROWS or row == 0:
            piece.make_king()  

            if piece.color == WHITE:
                self.white_kings += 1
            elif piece.color == RED:
                self.red_kings += 1