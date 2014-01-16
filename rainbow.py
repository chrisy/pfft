#!/usr/bin/env python

import led
import math

led.led_send([255, 255, 255])

incr = math.pi / led.rgb_count
incr = incr / 10

def s(t):
	return int((math.sin(t)+1.0)*63)+128

b = 0.0
while True:
	t = b
	p = []
	for count in range(led.rgb_count):
		p.append(s(t))
		p.append(s(t+math.pi/3))
		p.append(s(t+math.pi*2/3))
		t = t + incr

	led.rgb_send(p)

	b = b + incr
	if b >= (math.pi*2): b = 0.0
