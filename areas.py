#!/usr/bin/env python3

import math
def triangle(base, height):
	area = (1/2)*base*height
	return "Area of trianlge: " + str(area)

def rectangle(length, width):
	area = length*width
	return "Area of rectangle: " + str(area)

def square(side):
	area = side**2
	return "Area of square: " + str(area)

def circle(radius):
	area = math.pi*(radius**2)
	return "Area of circle: " + str(area)

def donut(outside_radius, inside_radius):
	area = math.pi*((outside_radius**2)-(inside_radius**2))
	return "Area of donut: " + str(area)
