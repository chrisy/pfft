#!/usr/bin/env python

import led
import math

led.led_send([255, 255, 255])

incr = math.pi * 2 / 1000

def s(t):
	return int((math.sin(t)+1.0)*127)

b = 0.0
while True:
	t = s(b)
	p = [ t, t, t ]
	led.led_send(p)

	b = b + incr
	if b >= (math.pi*2): b = 0.0
