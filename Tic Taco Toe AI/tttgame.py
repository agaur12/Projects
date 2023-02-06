import pygame as pg
import sys
import os
import tttbot as tb
from time import sleep, time

pg.init()

def one_player_game():
    bot_board = [
            [ '_', '_', '_' ],
            [ '_', '_', '_' ],
            [ '_', '_', '_' ]]

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    GAME_SIZE = (800, 640)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (50, 255, 50)
    BLUE = (50, 50, 255)
    RED = (255, 50, 50)
    REPLAY_MESSAGE = 'Press space to play again'
    
    pg.init()
    board_font = pg.font.SysFont('arial', 80)
    game_over_font = pg.font.SysFont('monospace', 80, bold=True)
    replay_font = pg.font.SysFont('monospace', 50)
    screen = pg.display.set_mode(GAME_SIZE)
    pg.display.set_caption('Tic Tac Toe')
    rect_width = int(GAME_SIZE[0] / 3)
    rect_height = int(GAME_SIZE[1] / 3)
    clock = pg.time.Clock()


    def draw_lines(screen, screen_size):
        vertical_line_1 = int(screen_size[0] / 3) 
        pg.draw.line(screen, BLACK, (vertical_line_1, 0), (vertical_line_1, screen_size[0]), 4)
        vertical_line_2 = vertical_line_1 * 2
        pg.draw.line(screen, BLACK, (vertical_line_2, 0), (vertical_line_2, screen_size[0]), 4)
        horizontal_line_1 = int(screen_size[1] / 3)
        pg.draw.line(screen, BLACK, (0, horizontal_line_1), (screen_size[0], horizontal_line_1), 4)
        horizontal_line_2 = horizontal_line_1 * 2
        pg.draw.line(screen, BLACK, (0, horizontal_line_2), (screen_size[0], horizontal_line_2), 4)


    def draw_letter(screen, letter, colour, position_rect):
        player_choice = board_font.render(letter, False, colour)
        choice_rect = player_choice.get_rect(center=position_rect.center)
        screen.blit(player_choice, choice_rect)


    def initialise_board(screen_size):
        board = []
        counter = 1
        for i in range(3):
            board.append([])
        rect_width = int(screen_size[0] / 3)
        rect_height = int(screen_size[1] / 3)
        top = 0
        for i in range(3):
            left = 0
            for j in range(3):
                board[i].append({
                    'played': False,
                    'player': '',
                    'rect': pg.Rect(left, top, rect_width, rect_height)
                })
                left += rect_width
                counter += 1
            top += rect_height
        return board


    def winner(board, player):
        for row in board:
            if (row[0]['player'] == player and row[1]['player'] == player and
                    row[2]['player'] == player):
                return True
        for i in range(3):
            if (board[0][i]['player'] == player and board[1][i]['player'] == player and
                    board[2][i]['player'] == player):
                return True
        if (board[0][0]['player'] == player and board[1][1]['player'] == player and
            board[2][2]['player'] == player):
            return True

        if (board[0][2]['player'] == player and board[1][1]['player'] == player and
            board[2][0]['player'] == player):
            return True

        return False


    def is_stalemate(board):
        return all([all([r['played'] for r in row]) for row in board])

    def user_click():
        x, y = pg.mouse.get_pos()
        mouse_click = pg.mouse.get_pressed()
        if (mouse_click[0] == True):
            if (x < rect_width):
                col = 0
            elif (x < rect_width * 2):
                col = 1
            elif(x < rect_width * 3):
                col = 2
            else:
                col = None
            if(y <  rect_height):
                row = 0
            elif (y < rect_height * 2):
                row = 1
            elif(y < rect_height * 3):
                row = 2
            else:
                row = None
            coordinates = (col, row)
            return coordinates

    def update(game, keys_pressed, userclick):
        someone_played = False
        if game['win'] or game['stalemate']:
            tb.reset_board(bot_board)
            return None
        elif game['player'] == 'O':
            best_move = tb.find_best_move(bot_board)
            game['board'][best_move[0]][best_move[1]]['played'] = True
            started = time()
            sleep(1)
            ended = time()
            game['board'][best_move[0]][best_move[1]]['player'] = game['player']
            bot_board[best_move[0]][best_move[1]] = game['player']
            print(bot_board)
            someone_played = True
        elif game['player'] == 'X':
            if ((keys_pressed[pg.K_1] or keys_pressed[pg.K_KP1] or userclick == (0, 0))
                    and not game['board'][0][0]['played']):
                game['board'][0][0]['played'] = True
                game['board'][0][0]['player'] = game['player']
                bot_board[0][0] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_2] or keys_pressed[pg.K_KP2] or userclick == (1, 0))
                    and not game['board'][0][1]['played']):
                game['board'][0][1]['played'] = True
                game['board'][0][1]['player'] = game['player']
                bot_board[0][1] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_3] or keys_pressed[pg.K_KP3] or userclick == (2, 0))
                    and not game['board'][0][2]['played']):
                game['board'][0][2]['played'] = True
                game['board'][0][2]['player'] = game['player']
                bot_board[0][2] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_4] or keys_pressed[pg.K_KP4] or userclick == (0, 1))
                    and not game['board'][1][0]['played']):
                game['board'][1][0]['played'] = True
                game['board'][1][0]['player'] = game['player']
                bot_board[1][0] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_5] or keys_pressed[pg.K_KP5] or userclick == (1, 1))
                    and not game['board'][1][1]['played']):
                game['board'][1][1]['played'] = True
                game['board'][1][1]['player'] = game['player']
                bot_board[1][1] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_6] or keys_pressed[pg.K_KP6] or userclick == (2, 1))
                    and not game['board'][1][2]['played']):
                game['board'][1][2]['played'] = True
                game['board'][1][2]['player'] = game['player']
                bot_board[1][2] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_7] or keys_pressed[pg.K_KP7] or userclick == (0, 2))
                    and not game['board'][2][0]['played']):
                game['board'][2][0]['played'] = True
                game['board'][2][0]['player'] = game['player']
                bot_board[2][0] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_8] or keys_pressed[pg.K_KP8]  or userclick == (1, 2))
                    and not (game['board'][2][1]['played'])):
                game['board'][2][1]['played'] = True
                game['board'][2][1]['player'] = game['player']
                bot_board[2][1] = game['player']
                someone_played = True

            elif ((keys_pressed[pg.K_9] or keys_pressed[pg.K_KP9] or userclick == (2, 2))
                    and not game['board'][2][2]['played']):
                game['board'][2][2]['played'] = True
                game['board'][2][2]['player'] = game['player']
                bot_board[2][2] = game['player']
                someone_played = True
        
        return someone_played

    def end_game_message(screen, screen_size, main_message, main_font,
            replay_message, replay_font, colour):
        main_text = main_font.render(main_message, False, colour)
        main_rect = main_text.get_rect(center=(screen_size[0]/2, screen_size[1]/2))
        screen.blit(main_text, main_rect)
        replay_text = replay_font.render(replay_message, False, colour)
        replay_rect = replay_text.get_rect(center=(screen_size[0]/2,
            main_rect.bottom + 30))
        screen.blit(replay_text, replay_rect)


    def render(screen, screen_size, game, clock):
        screen.fill(WHITE)
        draw_lines(screen, screen_size)
        for row in game['board']:
            for cell in row:
                if cell['player'] == 'X':
                    draw_letter(screen, 'X', BLUE, cell['rect'])
                elif cell['player'] == 'O':
                    draw_letter(screen, 'O', GREEN, cell['rect'])
                else:
                    draw_letter(screen, cell['player'], BLACK, cell['rect'])

        if game['win']:
            win_message = 'Player ' + game['player'] + ' won!'
            end_game_message(screen, GAME_SIZE, win_message, game_over_font,
                    REPLAY_MESSAGE, replay_font, RED)
        elif not game['win'] and game['stalemate']:
            stale_message = 'Stalemate!'
            end_game_message(screen, GAME_SIZE, stale_message, game_over_font,
                    REPLAY_MESSAGE, replay_font, RED)

        pg.display.update()
        clock.tick(60)


    def main():
        def initialise():
            return {
                    'board': initialise_board(GAME_SIZE),
                    'player': 'X',
                    'win': False,
                    'stalemate': False,
                    'change_player': False
                    }

        game = initialise()
        
        while True: 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            if game['player'] == 'X':
                keys_pressed = pg.key.get_pressed()
                userclick = user_click()
            else:
                keys_pressed = pg.key.get_pressed()
            if not (game['win'] or game['stalemate']):
                game['change_player'] = update(game, keys_pressed, userclick)

            else:
                if keys_pressed[pg.K_SPACE]:
                    game['change_player'] = update(game, keys_pressed, userclick)
                    game = initialise()
                    
            game['win'] = winner(game['board'], game['player'])
            game['stalemate'] = is_stalemate(game['board'])

            render(screen, GAME_SIZE, game, clock)

            if game['change_player'] and not (game['win'] or game['stalemate']):
                if game['player'] == 'X':
                    game['player'] = 'O'
                    
                else:
                    game['player'] = 'X'

    if __name__ == '__main__':
        main()

def two_player_game():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    GAME_SIZE = (800, 640)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (50, 255, 50)
    BLUE = (50, 50, 255)
    RED = (255, 50, 50)
    REPLAY_MESSAGE = 'Press space to play again'
    
    pg.init()
    board_font = pg.font.SysFont('arial', 80)
    game_over_font = pg.font.SysFont('monospace', 80, bold=True)
    replay_font = pg.font.SysFont('monospace', 50)
    screen = pg.display.set_mode(GAME_SIZE)
    pg.display.set_caption('Tic Tac Toe')
    rect_width = int(GAME_SIZE[0] / 3)
    rect_height = int(GAME_SIZE[1] / 3)
    clock = pg.time.Clock()


    def draw_lines(screen, screen_size):
        vertical_line_1 = int(screen_size[0] / 3) 
        pg.draw.line(screen, BLACK, (vertical_line_1, 0), (vertical_line_1, screen_size[0]), 4)
        vertical_line_2 = vertical_line_1 * 2
        pg.draw.line(screen, BLACK, (vertical_line_2, 0), (vertical_line_2, screen_size[0]), 4)
        horizontal_line_1 = int(screen_size[1] / 3)
        pg.draw.line(screen, BLACK, (0, horizontal_line_1), (screen_size[0], horizontal_line_1), 4)
        horizontal_line_2 = horizontal_line_1 * 2
        pg.draw.line(screen, BLACK, (0, horizontal_line_2), (screen_size[0], horizontal_line_2), 4)


    def draw_letter(screen, letter, colour, position_rect):
        player_choice = board_font.render(letter, False, colour)
        choice_rect = player_choice.get_rect(center=position_rect.center)
        screen.blit(player_choice, choice_rect)


    def initialise_board(screen_size):
        board = []
        counter = 1
        for i in range(3):
            board.append([])
        rect_width = int(screen_size[0] / 3)
        rect_height = int(screen_size[1] / 3)
        top = 0
        for i in range(3):
            left = 0
            for j in range(3):
                board[i].append({
                    'played': False,
                    'player': '',
                    'rect': pg.Rect(left, top, rect_width, rect_height)
                })
                left += rect_width
                counter += 1
            top += rect_height
        return board


    def winner(board, player):
        for row in board:
            if (row[0]['player'] == player and row[1]['player'] == player and
                    row[2]['player'] == player):
                return True
        for i in range(3):
            if (board[0][i]['player'] == player and board[1][i]['player'] == player and
                    board[2][i]['player'] == player):
                return True
        if (board[0][0]['player'] == player and board[1][1]['player'] == player and
            board[2][2]['player'] == player):
            return True

        if (board[0][2]['player'] == player and board[1][1]['player'] == player and
            board[2][0]['player'] == player):
            return True

        return False


    def is_stalemate(board):
        return all([all([r['played'] for r in row]) for row in board])

    def user_click():
        x, y = pg.mouse.get_pos()
        mouse_click = pg.mouse.get_pressed()
        if (mouse_click[0] == True):
            if (x < rect_width):
                col = 0
            elif (x < rect_width * 2):
                col = 1
            elif(x < rect_width * 3):
                col = 2
            else:
                col = None
            if(y <  rect_height):
                row = 0
            elif (y < rect_height * 2):
                row = 1
            elif(y < rect_height * 3):
                row = 2
            else:
                row = None
            coordinates = (col, row)
            return coordinates

    def update(game, keys_pressed, userclick):
        someone_played = False

        if ((keys_pressed[pg.K_1] or keys_pressed[pg.K_KP1] or userclick == (0, 0))
                and not game['board'][0][0]['played']):
            game['board'][0][0]['played'] = True
            game['board'][0][0]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_2] or keys_pressed[pg.K_KP2] or userclick == (1, 0))
                and not game['board'][0][1]['played']):
            game['board'][0][1]['played'] = True
            game['board'][0][1]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_3] or keys_pressed[pg.K_KP3] or userclick == (2, 0))
                and not game['board'][0][2]['played']):
            game['board'][0][2]['played'] = True
            game['board'][0][2]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_4] or keys_pressed[pg.K_KP4] or userclick == (0, 1))
                and not game['board'][1][0]['played']):
            game['board'][1][0]['played'] = True
            game['board'][1][0]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_5] or keys_pressed[pg.K_KP5] or userclick == (1, 1))
                and not game['board'][1][1]['played']):
            game['board'][1][1]['played'] = True
            game['board'][1][1]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_6] or keys_pressed[pg.K_KP6] or userclick == (2, 1))
                and not game['board'][1][2]['played']):
            game['board'][1][2]['played'] = True
            game['board'][1][2]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_7] or keys_pressed[pg.K_KP7] or userclick == (0, 2))
                and not game['board'][2][0]['played']):
            game['board'][2][0]['played'] = True
            game['board'][2][0]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_8] or keys_pressed[pg.K_KP8]  or userclick == (1, 2))
                and not (game['board'][2][1]['played'])):
            game['board'][2][1]['played'] = True
            game['board'][2][1]['player'] = game['player']
            someone_played = True

        elif ((keys_pressed[pg.K_9] or keys_pressed[pg.K_KP9] or userclick == (2, 2))
                and not game['board'][2][2]['played']):
            game['board'][2][2]['played'] = True
            game['board'][2][2]['player'] = game['player']
            someone_played = True

        return someone_played

    def end_game_message(screen, screen_size, main_message, main_font,
            replay_message, replay_font, colour):
        main_text = main_font.render(main_message, False, colour)
        main_rect = main_text.get_rect(center=(screen_size[0]/2, screen_size[1]/2))
        screen.blit(main_text, main_rect)
        replay_text = replay_font.render(replay_message, False, colour)
        replay_rect = replay_text.get_rect(center=(screen_size[0]/2,
            main_rect.bottom + 30))
        screen.blit(replay_text, replay_rect)


    def render(screen, screen_size, game, clock):
        screen.fill(WHITE)
        draw_lines(screen, screen_size)
        for row in game['board']:
            for cell in row:
                if cell['player'] == 'X':
                    draw_letter(screen, 'X', BLUE, cell['rect'])
                elif cell['player'] == 'O':
                    draw_letter(screen, 'O', GREEN, cell['rect'])
                else:
                    draw_letter(screen, cell['player'], BLACK, cell['rect'])

        if game['win']:
            win_message = 'Player ' + game['player'] + ' won!'
            end_game_message(screen, GAME_SIZE, win_message, game_over_font,
                    REPLAY_MESSAGE, replay_font, RED)
        elif not game['win'] and game['stalemate']:
            stale_message = 'Stalemate!'
            end_game_message(screen, GAME_SIZE, stale_message, game_over_font,
                    REPLAY_MESSAGE, replay_font, RED)

        pg.display.update()
        clock.tick(60)


    def main():
        def initialise():
            return {
                    'board': initialise_board(GAME_SIZE),
                    'player': 'X',
                    'win': False,
                    'stalemate': False,
                    'change_player': False
                    }

        game = initialise()
        
        while True: 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            keys_pressed = pg.key.get_pressed()
            userclick = user_click()
            if not (game['win'] or game['stalemate']):
                game['change_player'] = update(game, keys_pressed, userclick)
            else:
                if keys_pressed[pg.K_SPACE]:
                    game = initialise()
                    
            game['win'] = winner(game['board'], game['player'])
            game['stalemate'] = is_stalemate(game['board'])

            render(screen, GAME_SIZE, game, clock)

            if game['change_player'] and not (game['win'] or game['stalemate']):
                if game['player'] == 'X':
                    game['player'] = 'O'
                    
                else:
                    game['player'] = 'X'

    if __name__ == '__main__':
        main()

#one_player_game()

#two_player_game()