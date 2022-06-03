import pygame
from checkers.constant import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board



FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# name of game
pygame.display.set_caption('Checkers')

def get_row_column_from_mouse(position):

    x, y = position
    row = y // SQUARE_SIZE
    column = x // SQUARE_SIZE
    return row, column

def main():
    run = True
    # make clock to run game not too fast or slow. it runs actually based on hardware
    clock = pygame.time.Clock()
    board = Board()

    while run:
        # determine max FPS
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # get position when user click
                position = pygame.mouse.get_pos()
                # find row and column
                row, column = get_row_column_from_mouse(position)
                # get piece in there
                piece = board.get_piece(row, column)
                
                board.move(piece, 4 , 3)

        # make basic checkers window
        board.draw_window(WINDOW)
        pygame.display.update()

    pygame.quit()

        

if __name__ == "__main__":
    main()