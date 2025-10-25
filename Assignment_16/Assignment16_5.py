""" 5. Write a program to read a file line by line and display only those lines that contain
more than 5 words. """


import os
import sys
            
def DisplayLines(fobj):
    LineNo = 1
    print("Lines having words more tha 5 are : ")
    for Line in fobj:
        Words = Line.split()      
        if(len(Words) > 5):   
            print(f"Line {LineNo} : {Line.strip()}")
        LineNo += 1

def main():
    print("Enter the file name you want to read :")
    FileName = input()
    
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        print("file exists in the Directory.")
    else:
        print("There is no such file.")
        return
    
    fobj = open(FileName, "r")
    
    DisplayLines(fobj)
    
    fobj.close()
    
if __name__ == "__main__":
    main()