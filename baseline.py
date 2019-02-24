from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

message = "Hello! We are New Media Development :)"

def messageLoop(message):
	backColor = (randint(0,128), randint(0,128), randint(0,128))
	textColor = (randint(128,255), randint(128,255), randint(128,255))
	sense.show_message(message, text_colour=textColor, back_colour=backColor)
	messageLoop(message)
	
messageLoop(message)
