""" 4. Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory. Display execution time required for the
script.
Usage : DirectoryDusplicateRemoval.py “Demo”
Demo is name of directory. """

import os
import sys
import time
import hashlib

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path,'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)
            print("File name : ",os.path.relpath(fname))
            print("Checksum : ",checksum)
            print()

    Border = "-"*54
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectory Cleaner Script\n")

    fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")

def FindDuplicate(DirectoryName = "Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}
    
    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
                
        fobj = open("Log.txt","w")
        for checksum, fname in Duplicate.items():
            if(len(fname) >= 2):
                for File in fname:
                    fobj.write(f"{os.path.basename(File)} \n")
                    #print(os.path.basename(File))
                    
    return Duplicate
    
def DeleteDuplicate(DirectoryName = "Marvellous"):

    MyDict = FindDuplicate(DirectoryName)
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted file : ",os.path.basename(subvalue))
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    print("Total deleted file : ",Cnt)

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            start_time = time.time()
            
            Result= FindDuplicate(sys.argv[1])
            DeleteDuplicate(sys.argv[1])
            
            end_time = time.time()
            print("Time required for execution is : ", end_time - start_time)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()