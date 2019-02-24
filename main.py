#! /usr/env/python3
import pyautogui
import pygame
from math import sin, cos, pi, atan
from time import sleep

BLACK = (0,   0,   0)

WHITE = (255, 255, 255)
BLUE = (66, 134, 244)
LIGHT_BLUE = (66, 66, 66)

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("NEkey")

going = True

joystick = pygame.joystick.Joystick(0)
joystick.init()


speed = 1
vert_offset = 100

screenWidth, screenHeight = pyautogui.size()


mouseX, mouseY = pyautogui.position()


def moveMouse(x,y, oldX, oldY, speed):
	newX = oldX + (x*5)*(speed+2)*2
	newY = oldY + (y*5)*(speed+2)*2

	if newX > screenWidth:
		newX = screenWidth
	if newX < 0:
		newX = 0
	if newY > screenHeight:
		newY = screenHeight
	if newY < 0:
		newY = 0

	pyautogui.moveTo(newX, newY)
	return newX, newY


def joyOff(x,y,xOff, yOff):

	X = int(x*50)+xOff
	Y = int(y*50)+yOff

	pygame.draw.circle(screen, LIGHT_BLUE, (X, Y) , 20 )


def draw_ngon(Surface, color, n, radius, position):
	pi2 = 2 * 3.14

	for i in range(0, n):
		pygame.draw.line(Surface, color, position, (cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]))

	return pygame.draw.lines(Surface, color, True, [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])


def findDirect(x, y):
	y = -y

	if abs(x) < .6 and abs(y) < .6:
		return -1

	a = -1
	b = -1

	if x > 0 and y > 0:
		a = 0
		b = 1

	if x < 0 and y > 0:
		a = 3
		b = 2

	if x < 0 and y < 0:
		a = 4
		b = 5

	if x > 0 and y < 0:
		b = 6
		a = 7

	if abs(x) > abs(y):
		return a
	else:
		return b


def type(ax, ay, bx, by, c):
	a = findDirect(ax, ay)
	b = findDirect(bx, by)
	print(a, b)
	if a >= 0 and b >= 0:
		print(chr(97+b*8+a))
		sleep(0.07)
		return chr(97+b*8+a)
	print("NO VAL")
	return ""


def drawText(screen, text, x, y):
	font = pygame.font.SysFont("Comic Sans MS", 30)
	text = font.render(text, True, BLACK)
	screen.blit(text, (x, y))


def letters(screen,x, y, c):

	a = findDirect(x,y)

	drawText(screen, chr(97+a*8), 511, 94)
	drawText(screen, chr(97+a*8+1), 470, 55)
	drawText(screen, chr(97+a*8+2), 410, 54)
	drawText(screen, chr(97+a*8+3), 370, 92)
	drawText(screen, chr(97+a*8+4), 367, 152)
	drawText(screen, chr(97+a*8+5), 409, 197)
	drawText(screen, chr(97+a*8+6), 470, 194)
	drawText(screen, chr(97+a*8+7), 512, 156)

#a = 0
#b = 0

while going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill(WHITE)

	#pygame.draw.circle(screen, BLUE, (150, 150), 60)
	#pygame.draw.circle(screen, BLUE, (150*3, 150), 60)
	draw_ngon(screen, BLUE, 8, 60, (150, 150))
	draw_ngon(screen, BLUE, 8, 60, (150*3, 150))

	joyOff(joystick.get_axis(0), joystick.get_axis(1), 150, 150)
	joyOff(joystick.get_axis(3), joystick.get_axis(4), 150*3, 150)

	#print(findDirect(joystick.get_axis(0), joystick.get_axis(1)), joystick.get_axis(0), -joystick.get_axis(1))
	pyautogui.press(type(joystick.get_axis(3), joystick.get_axis(4), joystick.get_axis(0), joystick.get_axis(1), 0))

	#a-= joystick.get_axis(2)*0.01
	#b-= joystick.get_axis(5)*0.01

	letters(screen, joystick.get_axis(0), joystick.get_axis(1),0)

	#print(a, b)

	if joystick.get_button(0):
		mouseX, mouseY = moveMouse(joystick.get_axis(0), joystick.get_axis(1), mouseX, mouseY, joystick.get_axis(2))

	if joystick.get_button(5):
		pyautogui.click()

	pygame.display.flip()
