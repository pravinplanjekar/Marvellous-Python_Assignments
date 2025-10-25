""" 4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt """

import sys

def main():
    if(len(sys.argv) != 3):
        print("Insufficient number of arguments ")
        return
    
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]
    
    fobj1 = open(FileName1, "r")
    Data1 = fobj1.read()
    
    fobj2 = open (FileName2, "r")
    Data2 = fobj2.read()
    
    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")
    

if __name__ == "__main__":
    main()


