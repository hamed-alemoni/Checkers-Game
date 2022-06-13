import pygame
from .constant import WHITE, BLACK, RED, ROWS, COLUMNS, SQUARE_SIZE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    # this is evaluate function for minimax algorithm
    def evaluate(self):
        return self.white_left - self.red_left + (0.5 * (self.white_kings - self.red_kings))

    
    def get_all_pieces(self, color):
        
        pieces = []

        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces
        
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
        if row == ROWS - 1 or row == 0:
            piece.make_king()  

            if piece.color == WHITE:
                self.white_kings += 1
            elif piece.color == RED:
                self.red_kings += 1
    

    def remove(self, pieces):
        for piece in pieces:
            # make a square empty
            self.board[piece.row][piece.column] = 0

            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    # determine winner
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None 
    

    def get_valid_moves(self, piece):

        moves = {}

        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves
    
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[row][left]
            if current == 0:

                if skipped and not last:
                    break

                elif skipped:
                    moves[(row, left)] = last + skipped

                else:
                    moves[(row, left)] = last
                
                if last:

                    if step == -1:
                        row = max(row-3, 0)

                    else:
                        row = min(row+3, ROWS)

                    moves.update(self._traverse_left(row+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(row+step, row, step, color, left+1,skipped=last))

                break

            elif current.color == color:
                break

            else:
                last = [current]

            left -= 1
        
        return moves
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for row in range(start, stop, step):

            if right >= COLUMNS:
                break
            
            current = self.board[row][right]
            
            if current == 0:

                if skipped and not last:
                    break
                elif skipped:
                    moves[(row,right)] = last + skipped
                else:
                    moves[(row, right)] = last
                
                if last:
                    if step == -1:
                        row = max(row-3, 0)
                    else:
                        row = min(row+3, ROWS)
                    moves.update(self._traverse_left(row+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(row+step, row, step, color, right+1,skipped=last))

                break

            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves