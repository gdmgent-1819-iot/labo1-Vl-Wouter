from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

gridSize = range(0,8)

def createRect(x, y):
	rectColor = (randint(0,255), randint(0,255), randint(0,255))
	for i in range(0,y):
		
		if(i == 0):
			for j in range(0,x):
				sense.set_pixel(j, i, rectColor)
		elif(i == (y-1)):
			for j in range(0, x):
				sense.set_pixel(j, i, rectColor)
		else:
			sense.set_pixel(0, i, rectColor)
			sense.set_pixel((x-1), i, rectColor)

def growRect():
	for s in range(1,9):
		print("Size:", s)
		createRect(s, s)
		sleep = randint(1,3)
		time.sleep(sleep)
		sense.clear()
		
	shrinkRect()

def shrinkRect():
	sizes = [7, 6, 5, 4, 3, 2]
	for s in sizes:
		print("Size:", s)
		createRect(s, s)
		sleep = randint(1,3)
		time.sleep(sleep)
		sense.clear()
	growRect()

sense.clear()
growRect()


