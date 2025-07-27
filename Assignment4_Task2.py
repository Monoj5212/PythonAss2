"""
Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

with open("output.txt", "w") as file1:  # open output.txt file in writing mode.
    file1.write(input("Enter some text write to the file: ") + "\n")      # write the data to the file.
    print("Data successfully written to the file.")

with open("output.txt","a") as file1:   # open output.txt file in append mode.
    file1.write(input("Enter some text to append:") + "\n")               # append the data to the file.
    print("Data Successfully append to the file.")

with open("output.txt","r") as file1:   # open output.txt file in riding mode.
    print("Final content of the file:")
    print(file1.read())  # Use to read and print content of the file.