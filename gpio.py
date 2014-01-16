#!/usr/bin/env python

def _path(line):
	return "/sys/devices/virtual/gpio/gpio"+str(line)+"/"

def _read(line, type):
	file = open(_path(line)+type, "r")
	text = file.read()
	file.close()
	return text

def _write(line, type, value):
	file = open(_path(line)+type, "w")
	text = file.write(str(value)+"\n")
	file.close()

def dir(line, dir):
	if dir == 1: dir = "in"
	if dir == 0: dir = "out"
	_write(line, "direction", dir)

def set(line, val):
	_write(line, "value", val)

def get(line):
	return _read(line, "value")

