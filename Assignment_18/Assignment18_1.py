""" 1.Write a program which accepts file name from user and check whether that file exists in
current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not. """

import os

def main():
    print("Enter the name of file that you want to check : ")
    FileName = input()

    ret = os.path.exists(FileName)

    if(ret == True):
        print("File is present in the current directory")
    else:
        print("There is no such file")


if __name__ == "__main__":
    main()