from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
# return best score with best move
def minimax(position, depth, max_player, game):
    
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:

        max_eval = float('-inf')
        best_move = None

        for move in get_all_moves(position, WHITE, game):

            evaluation = minimax(move, depth-1, False, game)[0]

            max_eval = max(max_eval, evaluation)

            if max_eval == evaluation:
                best_move = move
        
        return max_eval, best_move
    else:

        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):

            evaluation = minimax(move, depth-1, True, game)[0]

            min_eval = min(min_eval, evaluation)

            if min_eval == evaluation:
                best_move = move
        
        return min_eval, best_move

# def find_eval_and_move(position, color, depth, game ,turn , min_or_max):

#     # initialize value of evaluate base on min or max
#     if turn:
#         evaluate = float('inf')
#     else:
#         evaluate = float('-inf')

#     best_move = None
#     for move in get_all_moves(position, color, game):

#         evaluation = minimax(move, depth, turn, game)[0]
#         evaluate = min_or_max(evaluate, evaluation)

#         if evaluate == evaluation:
#             best_move = move
    
    return evaluate, best_move
def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        # find valid moves for the piece
        valid_moves = board.get_valid_moves(piece)
        # (row, column) : [piece]
        for position, skip in valid_moves.items():

            # show simulation
            
            temp_board = deepcopy(board)

            temp_piece = temp_board.get_piece(piece.row, piece.column)

            new_board = simulation_move(temp_piece, position, temp_board, game, skip)

            moves.append(new_board)
    
    return moves

# simulate the move

def simulation_move(piece, position, board, game, skip):
    row, column = position
    # print(piece)

    board.move(piece, row, column)

    if skip:
        board.remove(skip)
    
    return board


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw_window(game.window)
    pygame.draw.circle(game.window, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)