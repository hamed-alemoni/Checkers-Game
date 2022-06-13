from .constant import RED, WHITE, GREY, SQUARE_SIZE, CROWN
import pygame
class Piece:

    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, column, color):
            self.row = row    
            self.column = column
            self.color = color
            self.king = False
            self.x = None
            self.y = None

            self.calculate_position()

    def calculate_position(self):
        # horizontal
        self.x = self.column * SQUARE_SIZE + SQUARE_SIZE // 2
        # vertical
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True
    
    # draw piece in appropriate square in board
    def draw_piece(self, window):

        radius = SQUARE_SIZE // 2 - self.PADDING
        # draw bigger circle
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.OUTLINE)
        # draw smaller circle
        pygame.draw.circle(window, self.color, (self.x, self.y) , radius)

        if self.king:
            # blit : put some image onto screen
            window.blit(CROWN, (self.x - CROWN.get_width() // 2 , self.y - CROWN.get_height() // 2))
            
    # move piece to new row and column then calculate position again
    def move_piece(self, row, column):

        self.row = row
        self.column = column
        self.calculate_position() 

    
    def __repr__(self):
        return str(self.color)


