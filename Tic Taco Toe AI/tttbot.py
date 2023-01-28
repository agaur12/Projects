import random

list = ('x', 'o')
rand_index = list.index(random.choice(list))
player = list[rand_index]
opponent = list[rand_index - 1]

board = [
        [ '_', '_', '_' ],
        [ '_', '_', '_' ],
        [ '_', '_', '_' ]] 

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
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if score != 0:
        return score
    if is_moves_left(board) == False:
        return score

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =='_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth+1, not isMax))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =='_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth+1, not isMax))
                    board[i][j] = '_'
        return best
    
def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    move_val = minimax(board, 0, True)
                    board[i][j] = '_'
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
    for i in range(3):
        for j in range(3):
            if best_move[0] == i:
                if best_move[1] == j:
                    board[i][j] = 'o'
                    print(board)
    print("The value of the best Move is :", best_val)
    return best_move
    

best_move = find_best_move(board)
print(best_move)
