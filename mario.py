from sense_hat import SenseHat
import time

sense = SenseHat()

o = (0, 0, 0)
b = (0, 0, 255)
r = (255, 0, 0)
s = (180, 124, 10) 

mario = [
o, o, o, o, o, o, o, o,
o, o, o, r, r, r, o, o,
o, o, o, s, s, o, o, o,
o, s, r, r, r, r, s, o,
o, o, o, b, b, o, o, o,
o, o, b, b, b, b, o, o,
o, o, b, o, o, b, o, o,
o, r, r, o, o, r, r, o,
]

mario_jump = [
o, o, o, r, r, r, o, o,
o, s, o, s, s, o, s, o,
o, o, r, r, r, r, o, o,
o, o, o, b, b, o, o, o,
o, o, o, b, b, o, r, o,
o, r, b, o, o, b, r, o,
o, r, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
]

sense.clear()
sense.set_pixels(mario)

def eventLoop():
	event = sense.stick.wait_for_event()
	if(event.action == "pressed" and event.direction == "up"):
		sense.set_pixels(mario_jump)
		time.sleep(1)
		sense.set_pixels(mario)
	if(event.action == "pressed" and event.direction == "down"):
		sense.clear()
		return 0
		
	eventLoop()
	
eventLoop()

