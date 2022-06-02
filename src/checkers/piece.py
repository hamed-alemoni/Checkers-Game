from .constant import RED, WHITE, SQUARE_SIZE

class Piece:
    def __init__(self, row, column, color):
            self.row = row    
            self.column = column
            self.color = color
            self.king = False
            
            if self.color == RED:
                self.direction = 1
            elif self.color == WHITE:
                self.direction = 0
            

            self.x = None
            self.y = None

    def calculate_position(self):
        # horizontal
        self.x = self.column * SQUARE_SIZE + SQUARE_SIZE // 2
        # vertical
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
