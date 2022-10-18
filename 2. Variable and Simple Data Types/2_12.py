# Name: Kyle Chan
# Date: 8/24/2022
# 2-10: This program displays the area and circumference for a circle with the radius of 12.

from math import pi

r = 12

area = pi * r ** 2
circumference = 2 * pi *r
print ("The area of a circle with radius",r,"is",area)
print ("The circumference of a circle with radius",r,"is","%.2f" % round(circumference, 2))