""" 2. Write a program to read and display the contents of a file data.txt. """
import sys

def main():
    print("Enter the name of the file you want to read : ")
    FileName = input()
    
    obj = open(FileName, "r")
    Data = obj.read()
    
    print(f"Data in the file {FileName} is : {Data}")

if __name__ == "__main__":
    main()