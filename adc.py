#!/usr/bin/env python

import spidev

speed = 1000000
bpw = 8

spi = spidev.SpiDev()
spi.open(0,1)
spi.bits_per_word = bpw
spi.lsbfirst = False
spi.mode = 0
spi.max_speed_hz = speed

def read(chan):
	cmd = [ 0x01, 0x80 | ((chan & 0x7) << 4), 0 ]
	result = spi.xfer2(cmd)
	return result[1] << 8 | result[2]

