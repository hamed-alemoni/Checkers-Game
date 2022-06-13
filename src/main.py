import pygame
from checkers.constant import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax

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
    game = Game(WINDOW)

    while run:
        # determine max FPS
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                # get position when user click
                position = pygame.mouse.get_pos()
                # find row and column
                row, column = get_row_column_from_mouse(position)
                
                if game.turn == RED:
                    
                    game.select(row, column)

        # make basic checkers window
        game.update()

    pygame.quit()

        

if __name__ == "__main__":
    main()