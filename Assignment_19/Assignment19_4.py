""" 4. Design automation script which accept two directory names and one file extension. Copy all
files with the specified extension from first directory into second directory. Second directory
should be created at run time.
Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
Demo is name of directory which is existing and contains files in it. We have to create new
Directory as Temp and copy all files with extension .exe from Demo to Temp."""

import os 
import sys 
import shutil

def CopyFilesToDirectory(SrcDirectoryName, DestDirectoryName):
    Flag = os.path.isabs(SrcDirectoryName)
    
    if(Flag == False):
        SrcDirectoryName = os.path.abspath(SrcDirectoryName)
        
    Flag = os.path.exists(SrcDirectoryName)
    
    if(Flag == False):
        print("Path is invalid")
        exit()
        
    Flag = os.path.isdir(SrcDirectoryName)
    
    if(Flag == False):
        print("Path is valid but Target is not a Directory")
        exit()
    
    Flag = os.path.exists(DestDirectoryName)
    
    if(Flag == False):
        os.mkdir(DestDirectoryName)
        print(f"New directory {DestDirectoryName} created sucessfully.")
        
    for fName in os.listdir(SrcDirectoryName):
        if(fName.endswith(sys.argv[3])):
            SrcPath = os.path.join(SrcDirectoryName, fName)
            DestPath = os.path.join(DestDirectoryName, fName)

            if os.path.isfile(SrcPath):
                shutil.copy(SrcPath, DestPath)
                #print(f"Copied : {fName}")

    print("All files copied successfully")

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
            CopyFilesToDirectory(sys.argv[1],sys.argv[2] )
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