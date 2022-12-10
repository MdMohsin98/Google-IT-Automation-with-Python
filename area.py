import math
def triangle(base, height):
    area = 1/2*base*height
    return "Area of triangle : " + str(round(area, 2))
def rectangle(length, width):
    area = length*width
    return "Area of rectangle : " + str(round(area, 2))
def circle(radius):
    area = math.pi * (radius**2)
    return "Area of circle : " + str(round(area, 2))
def donut(outside_radius, inside_radius):
    if inside_radius < outside_radius:
        area = math.pi * ((outside_radius**2) - (inside_radius**2))
        return "Area of donut : " + str(round(area, 2))
    else:
        print("Input outside_radius firstly then after inside_radius")
