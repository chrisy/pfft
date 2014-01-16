#!/usr/bin/env python

import led

led.led_send([255, 255, 255])

p = []
for count in range(led.rgb_count):
	p.append(128)
	p.append(128)
	p.append(128)
led.rgb_send(p)
