import pygame as pg
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
SCREEN_SIZE = (800, 640)

TITLE_POS = (250, 100)
ONEPLAYER_POS  = (300, 300) 
TWOPLAYER_POS = (300, 450)
CORNER_POS = (600, 10)
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

controlBar = Screen("Control Screen")

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
	controlBar.screenUpdate()
	mouse_pos = pg.mouse.get_pos()
	mouse_click = pg.mouse.get_pressed()
	keys = pg.key.get_pressed()
	if menuScreen.checkUpdate(CYAN):
		button_one = ONE_PLAYER_BUTTON.focusCheck(mouse_pos,
												mouse_click)
		button_two = TWO_PLAYER_BUTTON.focusCheck(mouse_pos,
												mouse_click)
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
		return_back = BACK_BUTTON.focusCheck(mouse_pos,
												mouse_click)
		BACK_BUTTON.showButton(onePlayerScreen.returnTitle())

		if return_back:
			onePlayerScreen.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
	
	elif twoPlayerScreen.checkUpdate(WHITE):
		return_back = BACK_BUTTON.focusCheck(mouse_pos,
												mouse_click)
		BACK_BUTTON.showButton(twoPlayerScreen.returnTitle())

		if return_back:
			twoPlayerScreen.endCurrentScreen()
			win = menuScreen.makeCurrentScreen()
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			done = True

	pg.display.update()
pg.quit()