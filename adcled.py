#!/usr/bin/env python

import sys, math, time
import adc, eq, gpio, led

while True:
	raw_l = adc.read(0)
	raw_r = adc.read(1)
	raw_eq = eq.read()

	l1 = 255-int(math.fabs(raw_l-512)/2)
	r1 = 255-int(math.fabs(raw_r-512)/2)

	l1 = 255
	l2 = 255

	led.led_send([l1, r1, l1])

	# l2 = (128-l1 / 2) + 128
	# r2 = (127-r1 / 2) + 128

	r = (raw_eq[0][0] + raw_eq[0][1] + raw_eq[1][0] + raw_eq[1][1]) / 4
	g = (raw_eq[0][2] + raw_eq[0][3] + raw_eq[1][2] + raw_eq[1][3]) / 4
	b = (raw_eq[0][5] + raw_eq[0][6] + raw_eq[1][5] + raw_eq[1][6]) / 4

	r = int(r/10)+128
	g = int(g/10)+128
	b = int(b/10)+128

	p = []
	for count in range(led.rgb_count):
		p.append(r)
		p.append(g)
		p.append(b)
	led.rgb_send(p)

	l = int(math.fabs(raw_l-512)/13)
	r = int(math.fabs(raw_r-512)/13)

	sys.stdout.write("\r")
	for i in range(l):
		sys.stdout.write('#')
	for i in range(39-l):
		sys.stdout.write(' ')
	for i in range(r):
		sys.stdout.write('#')
	for i in range(39-r):
		sys.stdout.write(' ')

	sys.stdout.write(repr(raw_eq)+"    ")
	
	sys.stdout.flush()
