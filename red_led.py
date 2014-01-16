#!/usr/bin/env python

import led

led.led_send([0, 0, 0])

p = []
for count in range(led.rgb_count):
	p.append(128)
	p.append(255)
	p.append(128)

led.rgb_send(p)
