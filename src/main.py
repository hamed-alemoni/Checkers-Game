import pygame
from checkers.constant import WIDTH, HEIGHT
from checkers.board import Board



FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# name of game
pygame.display.set_caption('Checkers')

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
                pass
        board.draw_squares(WINDOW)
        pygame.display.update()
    pygame.quit()

        

if __name__ == "__main__":
    main()