"""
Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""

num=int(input("Enter a number:"))

from math import *
SquareRoot=sqrt(num)
NatureLog=log(num,e)
NumSine=sin(num)

print("Square root of",num,"is:",SquareRoot)
print("Natural logarithm of",num,"is:",NatureLog)
print("Sin of",num,"is:",NumSine)