"""
 Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
try:    # use for File Not Found Error Handling
    my_file = open("sample.txt","r")    # Use to read sample.txt file and store my_file variable.
    redding1=my_file.read() # Use to read a file
    my_file.seek(0)  # Reset the file pointer to the beginning of the file

    redding2=my_file.readline() # Use to read (1st) one line file
    my_file.seek(0)  # Reset the file pointer to the beginning of the file

    redding3=my_file.readlines() # Use to read all line as list of the file
    my_file.seek(0)  # Reset the file pointer to the beginning of the file

    print(redding1)
    print(redding2)
    print(redding3)

    my_file.close() # Use to close file
except FileNotFoundError:
    print("The file 'sample.txt' does not exist.")   # If File Not Found then it will be print.