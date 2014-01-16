#!/usr/bin/env python

import sys, math, time
import adc, eq, gpio, led

bl = 32
bl2 = bl/2

h = []
m = 1024
m2 = m/2
m4 = m/4

adj = m4/128
for c in range(100):
	h.append(m2)

def peq(p):
	return "(%4d %4d %4d %4d %4d %4d %4d)" % tuple(p)

while True:
	raw_l = int(math.fabs(adc.read(0)-m2))
	raw_r = int(math.fabs(adc.read(1)-m2))
	raw_eq = eq.read()

	h.pop(0)
	h.pop(0)
	h.append(raw_l)
	h.append(raw_r)

	avg = float(sum(h)) / float(len(h))
	if avg != 0:
		gain = avg/128
	else:
		gain = 0.0

	raw_l = raw_l / gain
	raw_r = raw_r / gain

	if(raw_l >= 512): raw_l = 512
	if(raw_r >= 512): raw_r = 512

	r = (raw_eq[0][0] + raw_eq[0][1] + raw_eq[1][0] + raw_eq[1][1]) / 4
	g = (raw_eq[0][2] + raw_eq[0][3] + raw_eq[1][2] + raw_eq[1][3]) / 4
	b = (raw_eq[0][5] + raw_eq[0][6] + raw_eq[1][5] + raw_eq[1][6]) / 4

	r = r * gain
	g = g * gain
	b = b * gain

	r = r * adj
	g = g * adj
	b = b * adj

	if r > 127: r = 127
	if g > 127: g = 127
	if b > 127: b = 127

	r = int(r)+128
	g = int(g)+128
	b = int(b)+128


	p = []
	for count in range(led.rgb_count):
		p.append(r)
		p.append(g)
		p.append(b)
	led.rgb_send(p)

	l = int(raw_l/bl2)
	r = int(raw_r/bl2)

	sys.stdout.write("\r")
	for i in range(l):
		sys.stdout.write('#')
	for i in range((bl+2)-l):
		sys.stdout.write(' ')
	for i in range(r):
		sys.stdout.write('#')
	for i in range((bl+2)-r):
		sys.stdout.write(' ')

	sys.stdout.write(peq(raw_eq[0])+" "+peq(raw_eq[1])+" ")
	sys.stdout.write("%3.3f %3.3f %3.3f %3.3f    " % (gain, r, g, b))
	
	sys.stdout.flush()

