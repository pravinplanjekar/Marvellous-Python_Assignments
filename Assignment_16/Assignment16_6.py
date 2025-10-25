""" 6. Write a Python program to copy the contents of one file (source.txt) into another
file (destination.txt). """

import os

def main():
    print("Enter the name of source file that you want to read : ")
    SourceFileName = input()
    
    Flag = os.path.exists(SourceFileName)
    
    if(Flag == True):
        print(f" {SourceFileName} is present in the directory.")
        
        sobj = open(SourceFileName, "r")
        SData = sobj.read()
        
        print("Data has been read sucessfully.")
                
    else: 
        print("There is no such file in the directory.")
        return
    
    print("Enter the destination file in which you want to write :")
    DestinationFileName = input()
    
    Flag = os.path.exists(DestinationFileName)
    
    if(Flag == True):
        print(f"{DestinationFileName} is available in the Directory. ")
        
        dobj = open(DestinationFileName, "w")
        DData = dobj.write(SData)
        
        print(f"Data copied sucessfully from {SourceFileName} to {DestinationFileName}.")
        
    else: 
        print(f"{DestinationFileName} is not present in the Directory.")
    
    sobj.close()
    dobj.close()
    
if __name__ == "__main__":
    main()