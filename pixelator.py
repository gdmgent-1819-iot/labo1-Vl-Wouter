from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

gridSize = range(0,8)

def pixelator():
	for i in gridSize:
		for j in gridSize:
			sense.set_pixel(j, i, (randint(0,255), randint(0,255), randint(0,255)))
			time.sleep(0.2)
			sense.clear()
			
	pixelator()

pixelator()
