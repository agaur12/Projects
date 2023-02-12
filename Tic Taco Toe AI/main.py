import pygame as pg
import sys
import os
from time import sleep, time
import tttbot as tb

def one_player_game():
    started = time()
    sleep(1)
    ended = time()
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
    started = time()
    sleep(1)
    ended = time()
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


os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (800, 640)

TITLE_POS = (300, 100)
ONEPLAYER_POS  = (300, 300) 
TWOPLAYER_POS = (300, 450)
CORNER_POS = (600, 0)
BUTTON_SIZE = (200, 120)

CYAN = (224,255,255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
RED = (255, 50, 50)

class Screen():
	def __init__(self, title, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1],
				fill=(0, 0, 255)):
		self.height = height
		self.title = title
		self.width = width
		self.fill = fill
		self.CurrentState = False

	def makeCurrentScreen(self):
		pg.display.set_caption(self.title)
		self.CurrentState = True
		self.screen = pg.display.set_mode((self.width,
										self.height))

	def endCurrentScreen(self):
		self.CurrentState = False

	def checkUpdate(self, fill):
		self.fill = fill 
		return self.CurrentState

	def screenUpdate(self):
		if self.CurrentState:
			self.screen.fill(self.fill)

	def returnTitle(self):
		return self.screen

class Button():
	def __init__(self, x, y, sx, sy, bcolour, fbcolour,
				font, fcolour, text):
		self.x = x
		self.y = y
		self.sx = sx
		self.sy = sy
		self.fontsize = 25
		self.bcolour = bcolour
		self.fbcolour = fbcolour
		self.fcolour = fcolour
		self.text = text
		self.CurrentState = False
		self.buttonf = pg.font.SysFont(font,
									self.fontsize)

	def showButton(self, display):
		if(self.CurrentState):
			pg.draw.rect(display, self.fbcolour,
						(self.x, self.y, self.sx, self.sy))
		  
		else:
			pg.draw.rect(display, self.fbcolour,
						(self.x, self.y, self.sx, self.sy))
		textsurface = self.buttonf.render(self.text,
										False,
										self.fcolour)
		display.blit(textsurface, ((self.x + (self.sx/2) -
									(self.fontsize/2)*(len(self.text)/2)
									- 5, (self.y + (self.sy/2)
										- (self.fontsize/2)-4))))
	def focusCheck(self, mousepos, mouseclick):
		if(mousepos[0] >= self.x and mousepos[0]
			<= self.x + self.sx and mousepos[1] >= self.y
				and mousepos[1] <= self.y + self.sy):
			self.CurrentState = True
			return mouseclick[0]

		else:
			self.CurrentState = False
			return False
			
class Title(Button):
  def __init__(self, x, y, sx, sy, bcolour, fbcolour, font, fcolour, text):
			self.x = x
			self.y = y
			self.sx = sx
			self.sy = sy
			self.fontsize = 100
			self.bcolour = bcolour
			self.fbcolour = fbcolour
			self.font = font
			self.fcolour = fcolour
			self.text = text
			self.CurrentState = False
			self.buttonf = pg.font.SysFont(font, self.fontsize)
				  

pg.init()
pg.font.init()

menuScreen = Screen("Menu Screen")

twoPlayerScreen = Screen("One Player Screen")

onePlayerScreen = Screen("Two Player Screen")

win = menuScreen.makeCurrentScreen()

TITLE_BUTTON = Title(TITLE_POS[0], TITLE_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
						CYAN, "TimesNewRoman",
						(50, 50, 255), "TIC TAC TOE")

ONE_PLAYER_BUTTON = Button(ONEPLAYER_POS[0], ONEPLAYER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "One Player")
					
TWO_PLAYER_BUTTON = Button(TWOPLAYER_POS[0], TWOPLAYER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Two Player")

BACK_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
						BLACK, "TimesNewRoman",
						(255, 255, 255), "Back")

done = False
toggle = False

while not done:
	menuScreen.screenUpdate()
	onePlayerScreen.screenUpdate()
	twoPlayerScreen.screenUpdate()
	mouse_pos = pg.mouse.get_pos()
	mouse_click = pg.mouse.get_pressed()
	keys = pg.key.get_pressed()
	if menuScreen.checkUpdate(CYAN):
		button_one = ONE_PLAYER_BUTTON.focusCheck(mouse_pos, mouse_click)
		button_two = TWO_PLAYER_BUTTON.focusCheck(mouse_pos, mouse_click)
		ONE_PLAYER_BUTTON.showButton(menuScreen.returnTitle())
		TWO_PLAYER_BUTTON.showButton(menuScreen.returnTitle())
		TITLE_BUTTON.showButton(menuScreen.returnTitle())

		if button_one:
			win = onePlayerScreen.makeCurrentScreen()
			menuScreen.endCurrentScreen()
		if button_two:
			win = twoPlayerScreen.makeCurrentScreen()
			menuScreen.endCurrentScreen()

	elif onePlayerScreen.checkUpdate(WHITE):
		one_player_game()
	elif twoPlayerScreen.checkUpdate(WHITE):
		two_player_game()
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			done = True

	pg.display.update()
pg.quit()