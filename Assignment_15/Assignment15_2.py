""" 2. Write a program which accept file name from user and open that file and display the contents
of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console. """

import os

def main():
    print("Enter the file name that you want to read :")
    FileName = input()
    
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        print("File is present in the directory.")
        fobj = open(FileName,"r")
        Data = fobj.read()
        
        print("Data from the file is : ",Data)
        
        fobj.close()
    else:
        print("there is no such file")

if __name__ == "__main__":
    main()