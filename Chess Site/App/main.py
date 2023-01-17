import chess
import chess.svg
import fastapi


def choose_color(color='white'):
    match color:
        case 'white':
            chess.WHITE
        case 'black':
            chess.Black
        case _:
            print("Pick Black or White")
            choose_color(color='white')

choose_color(input())

board = chess.Board()
svg_board = chess.svg.board(
    board,
    fill=dict.fromkeys(board.attacks(chess.E4), "#cc0000cc"),
    arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
    squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
    size=350, 
) 

print(svg_board)

board.legal_moves

game_start = True


game_over = False

board.can_claim_threefold_repetition()
board.can_claim_fifty_moves()
board.can_claim_draw()