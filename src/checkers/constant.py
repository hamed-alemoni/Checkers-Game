import pygame

WIDTH, HEIGHT = 800, 800

ROWS, COLUMNS = 8, 8

SQUARE_SIZE = WIDTH // COLUMNS

# rgb format

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png') , (40, 25))