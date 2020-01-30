#Write a program Distance.java that takes two integer command­line arguments x
#and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
#formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function

import math

a = int(input('Enter the x-coordinate: '))
b = int(input('Enter the y-coordinate: '))

def distance(x,y):
  return math.sqrt(x*x + y*y)

print(f"The Euclidean distance from the point ({a},{b}) to the origin (0, 0) is : {distance(a,b)}")  
