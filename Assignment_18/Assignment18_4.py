""" 4.Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt """

import sys

def main():
    if(len(sys.argv) != 3):
        print("Insufficient number of arguments")
        return

    SourceFileName = sys.argv[1]
    DestinationFileName = sys.argv[2]
    
    sobj = open(SourceFileName, "r")
    SData = sobj.read()
    
    dobj = open(DestinationFileName, "r")
    DData = dobj.read()
    
    if(SData == DData):
        print("Sucess....")
    else:
        print("Failure...")

    sobj.close()
    dobj.close()

if __name__ == "__main__":
    main()
    