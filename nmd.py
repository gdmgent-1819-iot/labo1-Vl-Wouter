from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

letters = ["N", "M", "D"]

def letterLoop():
	for i in letters:
		color = (randint(0,255), randint(0,255), randint(0,255))
		sense.show_letter(i, text_colour=color)
		time.sleep(1)
	time.sleep(1)
	letterLoop()
	
letterLoop()


