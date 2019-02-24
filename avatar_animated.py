from sense_hat import SenseHat
import time
from random import randint, random

sense = SenseHat()

def genAvatar():
	fillColor = (randint(0,255), randint(0,255), randint(0,255))
	for i in range(0,4):
		for j in range(0,8):
			chance = random()
			if(chance > 0.5):
				sense.set_pixel(i,j,fillColor)
				sense.set_pixel((7-i), j, fillColor)
	time.sleep(1)
	sense.clear()
	genAvatar()
				
genAvatar()
				
	
