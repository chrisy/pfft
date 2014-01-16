#!/usr/bin/env python

import spidev
import gpio

speed = 1000000
bpw = 8

spi = spidev.SpiDev()
spi.open(0,0)
spi.bits_per_word = bpw
spi.lsbfirst = False
spi.mode = 0
spi.max_speed_hz = speed

gpio.dir(25, "out")

# WS2801 methods

led_count = 3

def led_send(values):
	gpio.set(25, 0)
	spi.xfer2(values, speed, 500, bpw)

# The other RGB thing methods

rgb_count = 32*5
rgb_clear_count = int((rgb_count+31)/32)

def rgb_reset():
	buf = []
	for i in range(rgb_clear_count):
		buf.append(0)
	gpio.set(25, 1)
	spi.xfer2(buf, speed, 500, bpw)

rgb_reset()

def rgb_send(values):
	gpio.set(25, 1)
	spi.xfer2(values, speed, 500, bpw)
	rgb_reset()


