player, bot = 'X', 'O'

def reset_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j]= '_'
        
    return None

def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(board):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            if board[row][0] == bot:
                return 1
            elif board[row][0] == player:
                return -1

    for column in range(3):
        if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
            if board[0][column] == bot:
                return 1
            elif board[0][column] == player:
                return -1     
    
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if board[0][0] == bot:
            return 1
        elif board[0][0] == player:
            return -1
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[0][2] == bot:
            return 1
        elif board[0][2] == player:
            return -1
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if score != 0:
        return score
    if is_moves_left(board) == False:
        return score

    if isMax:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =='_':
                    board[i][j] = bot
                    max_score = minimax(board, depth + 1, False)
                    if max_score > best_score:
                        best_score = max_score
                    board[i][j] = '_'
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] =='_':
                    board[i][j] = player
                    min_score = minimax(board, depth + 1, True)
                    if min_score < best_score:
                        best_score = min_score
                    board[i][j] = '_'
        return best_score

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = bot
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = bot 
    return best_move
