""" 3.Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt """

import sys

def main():
    if(len(sys.argv) != 3):
        print("Insufficient number of arguments")
        return

    SourceFileName = sys.argv[1]
    DestinationFileName = sys.argv[2]
    
    sobj = open(SourceFileName, "r")
    SData = sobj.read()
    
    dobj = open(DestinationFileName, "w")
    DData = dobj.write(SData)
    
    print("data copied sucessfully")

    sobj.close()
    dobj.close()

if __name__ == "__main__":
    main()
    