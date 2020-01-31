# 16. Write a program WindChill.java that takes two double command­line arguments t
# and v and prints the wind chill. Use Math.pow(a, b) to compute ab.
# Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
# the National Weather Service defines the effective temperature (the wind chill) to
# be:
# w = 35.74 + .6215t + (.4275t - 35.75)*(v**.16)
# Note : the formula is not valid if t is larger than 50 in absolute value or if v is larger
# than 120 or less than 3 (you may assume that the values you get are in that range).

import math

t = float(input("Enter the temperature in Fahrenheit less than 50F: "))
while t > 50:
        print("Please input a valid temperature: ")
        t = float(input("Enter the temperature in Fahrenheit less than 50F: "))


v = float(input("Enter the wind speed(miles per hour between 3 miles per hour and 120 miles per hour): "))
while v > 120 or v < 3:
        print("Please input a valid speed: ")
        v = float(input("Enter the wind speed(miles per hour): "))

def windchill(t,v):
    w = 35.74 + .6215*t + (.4275*t - 35.75)*(pow(v,.16))
    return w

print(f"The windchill is {windchill(t,v)}")