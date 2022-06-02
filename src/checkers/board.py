import pygame
from .constant import BLACK, RED, ROWS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_peace = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
    
    def draw_squares(self, window : pygame):
        
        window.fill(BLACK)

        for row in range(ROWS):
            for column in range(row % 2 , ROWS, 2):
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, column * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                #                                  position x            position y         size of edges             