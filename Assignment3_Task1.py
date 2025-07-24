"""
Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

num=int(input("Enter any number:"))

def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num-1)

result=fact(num)

print("The factorial value of ",num,"is:",result)