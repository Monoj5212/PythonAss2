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

# PythonAss4_Task1

try:                                    # use for File Not Found Error Handling
    my_file = open("sample.txt","r")    # Use to read sample.txt file and store my_file variable.
    redding1=my_file.read()             # Use to read a file
    my_file.seek(0)                     # Reset the file pointer to the beginning of the file

    redding2=my_file.readline()         # Use to read (1st) one line file
    my_file.seek(0)                     # Reset the file pointer to the beginning of the file

    redding3=my_file.readlines()         # Use to read all line as list of the file
    my_file.seek(0)                      # Reset the file pointer to the beginning of the file

    print(redding1)
    print(redding2)
    print(redding3)

    my_file.close() # Use to close file
except FileNotFoundError:
    print("The file 'sample.txt' does not exist.") # If File Not Found then it will be print.


# PythonAss4_Task2

with open("output.txt", "w") as file1:                                      # open output.txt file in writing mode.
    file1.write(input("Enter some text write to the file: ") + "\n")        # write the data to the file.
    print("Data successfully written to the file.")

with open("output.txt","a") as file1:                                     # open output.txt file in append mode.
    file1.write(input("Enter some text to append:") + "\n")               # append the data to the file.
    print("Data Successfully append to the file.")

with open("output.txt","r") as file1:                                     # open output.txt file in riding mode.
    print("Final content of the file:")
    print(file1.read())  # Use to read and print content of the file.
