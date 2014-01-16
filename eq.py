#!/usr/bin/env python

import adc, gpio

gpio.dir(23, "out")
gpio.dir(24, "out")

def read():
	# Send a reset signal
	gpio.set(24, 1)
	gpio.set(23, 1)
	gpio.set(23, 0)
	gpio.set(24, 0)

	l = []
	r = []

	for i in range(7):
		gpio.set(23, 1)
		gpio.set(23, 0)
		l.append(adc.read(2))
		r.append(adc.read(3))

	return [l, r]

