import pygame as pg
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (800, 640)

CORNER_POS = (600, 10)
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

normalPlayScreen = Screen("Strategic Tic Tac Toe Play Screen")

strategicPlayScreen

normalTicTactToeScreen

strategicTicTactToeScreen

smallBoardScreen

mediumBoardScreen

largeBoardScreen

control_bar = Screen("Control Screen")

win = menuScreen.makeCurrentScreen()

MENU_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")

PLAY_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")

ONE_PLAYER_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")
					
TWO_PLAYER_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
					BLACK, "TimesNewRoman",
					(255, 255, 255), "Play")

BACK_BUTTON = Button(CORNER_POS[0], CORNER_POS[1], BUTTON_SIZE[0], BUTTON_SIZE[1], (0, 0, 0),
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