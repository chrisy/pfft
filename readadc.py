#!/usr/bin/env python

import sys, math, time
import adc, eq, gpio, led

while True:
	l = int(math.fabs(adc.read(0)-512)/13)
	r = int(math.fabs(adc.read(1)-512)/13)
	sys.stdout.write("\r")
	for i in range(l):
		sys.stdout.write('#')
	for i in range(39-l):
		sys.stdout.write(' ')
	for i in range(r):
		sys.stdout.write('#')
	for i in range(39-r):
		sys.stdout.write(' ')

	sys.stdout.write(repr(eq.read())+"    ")
	
	sys.stdout.flush()
