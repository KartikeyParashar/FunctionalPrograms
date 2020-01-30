# Write a program Quadratic.py to find the roots of the equation a*x*x + b*x + c.
# Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
# can  be  found  using  a  formula
# delta  =  b*b -­ 4*a*c
# Root  1  of  x  =  (­b  +  sqrt(delta))/(2*a)
# Root  2  of  x  =  (­b  ­  sqrt(delta))/(2*a)
# Take  a,  b  and  c  as  input  values  to  find  the  roots  of  x

import cmath

def roots_of_quadratic(a, b, c):
  delta = b ** 2 - 4 * a * c
  
  sol1 = (-b - cmath.sqrt(delta)) / (2 * a) 
  sol2 = (-b + cmath.sqrt(delta)) / (2 * a)
  return f"The roots are {sol1} and {sol2}"

x = int(input("Enter the first value except zero: "))
y = int(input("Enter the second value: "))
z = int(input("Enter the third value:  "))

while True:
  if x != 0:
    print(roots_of_quadratic(x, y, z))
    break
  else:
    print("Please enter a valid value of x: ")
    x = int(input("Enter the first value except zero: "))
