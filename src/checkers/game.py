import pygame
from .constant import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, window):
        self._init()
        self.window = window
    
    def _init(self):

        self.selected_piece = None
        self.valid_moves = {}
        self.board = Board()
        self.turn = RED

    def update(self):
        self.board.draw_window(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()
    

    def select(self, row, column):

        if self.selected_piece:
            result = self._move(row, column)
            if not result:
                self.selected_piece = None
                self.select(row, column)
        
        piece = self.board.get_piece(row, column)
        if piece != 0 and self.turn == piece.color:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    def _move(self, row, column):
        # get piece that we want move to
        piece = self.board.get_piece(row, column)
        # the piece is empty and the row and column are in valid moves
        if self.selected_piece and piece == 0 and (row , column) in self.valid_moves:
            self.board.move(self.selected_piece, row, column)
            skipped = self.valid_moves[(row, column)]

            if skipped:
                self.board.remove(skipped)

            self.change_turn()
        else:
            return False

        return True 


    def change_turn(self):

        self.valid_moves = {}

        if self.turn == WHITE:
            self.turn = RED
        else:
            self.turn = WHITE
        # self.turn = RED if self.turn == WHITE else self.turn = WHITE
    
    def winner(self):
        return self.board.winner()
    

    def draw_valid_moves(self, moves):
        for move in moves:
            row, column = move
            pygame.draw.circle(self.window, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)