player, opponent = x, o

def is_moves_left(board):
    for i in range(3):
        for j in rang(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(b):
    



board = [     
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ] ]

is_moves_left(board)
bestMove = find_best_move(board)