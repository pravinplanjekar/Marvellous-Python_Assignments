""" 8. Write a script to remove all blank lines from a file. Save the cleaned output to a
new file. """

import os 

def main():
    print("Enter the name of file :")
    FileName = input()
    
    Flag = os.path.exists(FileName)
    
    if(Flag == True):
        print("file exists in the Directory.")
    else:
        print("There is no such file.")
        
    fobj = open(FileName, "r")
    DataLines = fobj.readlines()
    
    print("Enter the name of file in which you want to write the data : ")
    DestFileName = input()
    
    dobj = open(DestFileName, "w")
    
    for line in DataLines:
        if(line.strip() != ""):
            dobj.write(line)
            
    print("Data written sucessfully.")
    
if __name__ == "__main__":
    main()