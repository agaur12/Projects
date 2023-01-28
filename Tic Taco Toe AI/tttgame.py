import pygame as pg
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (800, 640)

BUTTON_POS = (600, 10)
BUTTON_SIZE = (200, 100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
RED = (255, 50, 50)

REPLAY_MESSAGE = 'Press space to play again'

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

pg.init()
pg.font.init()

menuScreen = Screen("Menu Screen")

playScreen = Screen("Play Screen")

control_bar = Screen("Control Screen")

win = menuScreen.makeCurrentScreen()

ONE_PLAYER_BUTTON = Button(BUTTON_POS[0], BUTTON_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")
					
TWO_PLAYER_BUTTON = Button(BUTTON_POS[0], BUTTON_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")

BACK_BUTTON = Button(BUTTON_POS[0], BUTTON_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
						BLACK, "TimesNewRoman",
						(255, 255, 255), "Back")

done = False
toggle = False

while not done:
	menuScreen.screenUpdate()
	control_bar.screenUpdate()
	mouse_pos = pg.mouse.get_pos()
	mouse_click = pg.mouse.get_pressed()
	keys = pg.key.get_pressed()
	if menuScreen.checkUpdate(WHITE):
		control_barbutton = ONE_PLAYER_BUTTON.focusCheck(mouse_pos,
												mouse_click)
		ONE_PLAYER_BUTTON.showButton(menuScreen.returnTitle())

		if control_barbutton:
			win = control_bar.makeCurrentScreen()
			menuScreen.endCurrentScreen()

	elif control_bar.checkUpdate(WHITE):
		return_back = BACK_BUTTON.focusCheck(mouse_pos,
												mouse_click)
		BACK_BUTTON.showButton(control_bar.returnTitle())

		if return_back:
			control_bar.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			done = True

	pg.display.update()
pg.quit()

"""from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
import sys
from PyQt5 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("Tic Tac Toe")
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()

mySlider = QSlider(Qt.Horizontal, self)
mySlider.setGeometry(30, 40, 200, 30)
mySlider.valueChanged[int].connect(self.changeValue)"""

"""
pg.init()
board_font = pg.font.SysFont('arial', 80)
game_over_font = pg.font.SysFont('monospace', 80, bold=True)
replay_font = pg.font.SysFont('monospace', 50)
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption('Tic Tac Toe')
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
                'player': str(counter), 
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


def update(game, keys_pressed):
    someone_played = False
    if ((keys_pressed[pg.K_1] or keys_pressed[pg.K_KP1])
            and not game['board'][0][0]['played']):
        game['board'][0][0]['played'] = True
        game['board'][0][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_2] or keys_pressed[pg.K_KP2])
            and not game['board'][0][1]['played']):
        game['board'][0][1]['played'] = True
        game['board'][0][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_3] or keys_pressed[pg.K_KP3])
            and not game['board'][0][2]['played']):
        game['board'][0][2]['played'] = True
        game['board'][0][2]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_4] or keys_pressed[pg.K_KP4])
            and not game['board'][1][0]['played']):
        game['board'][1][0]['played'] = True
        game['board'][1][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_5] or keys_pressed[pg.K_KP5])
            and not game['board'][1][1]['played']):
        game['board'][1][1]['played'] = True
        game['board'][1][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_6] or keys_pressed[pg.K_KP6])
            and not game['board'][1][2]['played']):
        game['board'][1][2]['played'] = True
        game['board'][1][2]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_7] or keys_pressed[pg.K_KP7])
            and not game['board'][2][0]['played']):
        game['board'][2][0]['played'] = True
        game['board'][2][0]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_8] or keys_pressed[pg.K_KP8])
            and not game['board'][2][1]['played']):
        game['board'][2][1]['played'] = True
        game['board'][2][1]['player'] = game['player']
        someone_played = True

    elif ((keys_pressed[pg.K_9] or keys_pressed[pg.K_KP9])
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
        end_game_message(screen, SCREEN_SIZE, win_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)
    elif not game['win'] and game['stalemate']:
        stale_message = 'Stalemate!'
        end_game_message(screen, SCREEN_SIZE, stale_message, game_over_font,
                REPLAY_MESSAGE, replay_font, RED)

    pg.display.update()
    clock.tick(60)


def main():
    def initialise():
        return {
                'board': initialise_board(SCREEN_SIZE),
                'player':  'X',
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
        if not (game['win'] or game['stalemate']):
            game['change_player'] = update(game, keys_pressed)
        else:
            if keys_pressed[pg.K_SPACE]:
                game = initialise()

        game['win'] = winner(game['board'], game['player'])
        game['stalemate'] = is_stalemate(game['board'])

        render(screen, SCREEN_SIZE, game, clock)
        if game['change_player'] and not (game['win'] or game['stalemate']):
            if game['player'] == 'X':
                game['player'] = 'O'
            else:
                game['player'] = 'X'

if __name__ == '__main__':
    main()

"""