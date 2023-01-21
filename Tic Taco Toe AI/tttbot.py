player, opponent = 'x', 'o'

def is_moves_left(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == '_':
                return True
    return False

def evaluate(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10
 
    for column in range(3):
        if (b[0][column] == b[1][column] and b[1][column] == b[2][column]):
            if b[0][column] == player:
                return 10
            elif b[0][column] == opponent:
                return -10       
    
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if b[0][0] == player:
                return 10
        elif b[0][0] == opponent:
            return -10 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if b[0][2] == player:
                return 10
        elif b[0][2] == opponent:
            return -10 

board = [   
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]] 

print(evaluate(board))
#bestMove = find_best_move(board)