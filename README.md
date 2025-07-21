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
