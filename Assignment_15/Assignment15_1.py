""" 1.Write a program which accepts file name from user and check whether that file exists in current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not. """

import os

def main():
    print("Enter the file name which you want to check : ")
    FileName = input()
    
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        print("File is present in the current directory.")
    else:
        print("File is not present in the current directory.")
 

if __name__ == "__main__":
    main()