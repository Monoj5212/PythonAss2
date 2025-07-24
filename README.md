# PythonAss2_Task1

a=int(input("Enter a Number to Check Odd or Even:"))   # Take input number in "a" variable.
if a%2==0:                                             # a variable % by 2 for reminder value & result (reminder) compared with 0 using double == sign.
    print(a,"is Even number.")
else:
    print(a,"is Odd number.")

# PythonAss2_Task2

add=0                                          # "add" variable assing to 0 ("zero") due to line 13
for a in range(1,51):                          # for etration for 1 to 50 range.
    add=add+a                                  # value of "a" storing in add variable.
print("The sum of numbers 1 to 50 is:",add)


# PythonAss3_Task1

num=int(input("Enter any number:"))            # Take input in "num" variable.

def fact(num):                                 # function define fact()
    if num < 2:                                # checking the input value is <2 or >2
        return 1
    else:
        return num * fact(num-1)                # performing recursion.

result=fact(num)                                # function calling.

print("The factorial value of ",num,"is:",result) # printing result/output.


# PythonAss3_Task2

num=int(input("Enter a number:"))                    # Take input in "num" variable.

from math import *                                   # importing all from math module
SquareRoot=sqrt(num)                                 # Square root of the number using sqrt()
NatureLog=log(num)                                   # Natural logarithm (log base e) of the number using log()
NumSine=sin(num)                                     # Sine of the number (in radians) using sin()

print("Square root of",num,"is:",SquareRoot)
print("Natural logarithm of",num,"is:",NatureLog)
print("Sin of",num,"is:",NumSine)
