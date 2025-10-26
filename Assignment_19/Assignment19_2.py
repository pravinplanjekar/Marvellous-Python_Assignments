""" 2. Design automation script which accept directory name and two file extensions from user.
Rename all files with first file extension with the second file extenntion.
Usage : DirectoryRename.py “Demo” “.txt” “.doc”
Demo is name of directory and .txt is the extension that we want to search and rename
with .doc.
After execution this script each .txt file gets renamed as .doc. """

import os 
import sys 
import time 

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Flag = os.path.isabs(DirectoryName)
    
    if(Flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
        
    Flag = os.path.exists(DirectoryName)
    
    if(Flag == False):
        print("Path is invalid")
        exit()
        
    Flag = os.path.isdir(DirectoryName)
    
    if(Flag == False):
        print("Path is valid but Target is not a Directory")
        exit()
    
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fName in FileNames:
            if fName.endswith(sys.argv[2]):
                
                OldPath = os.path.join(FolderName, fName)
                NewName = fName[:-len(sys.argv[2])] + (sys.argv[3])
                NewPath = os.path.join(FolderName, NewName)

                os.rename(OldPath, NewPath)

def main():
    Border = "-"*54
    print(Border)
    print("-------------------------Marvellous Automation-----------------")
    print(Border)
    
    if(len(sys.argv) == 4):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This applcation is to perform directory cleaning")
            print("This is directory automation script")
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")
        else:
            DirectoryWatcher(sys.argv[1])
    else:
        print("Invalid numberof command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : used to display the usage")
        
    print(Border)
    print("-------------------Thank you for using our script-----------------------")
    print("------------------------Marvellous Infosystems--------------------")
    print(Border)
            
if __name__ == "__main__":
    main()