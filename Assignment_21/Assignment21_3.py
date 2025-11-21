""" 3. Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory. """

import psutil
import os
import time
import sys

def CreateLog(FolderName, Data):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")
    
    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")

    border = "-"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border + "\n")

    for value in Data:
        fobj.write("%s \n\n" %value)

    fobj.write(border)

    fobj.close()

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h"):
            print("This application is used to create a long of running processes")
            return
        
        if(sys.argv[1] == "--u"):
            print("Execute the code as : ")
            print("python Filename.py Directory Name")
            return

    if(len(sys.argv) != 2):
        print("Insufficient number of arguments")
        print("You can use --h for help as --u for usage")
        return
    
    DirName = sys.argv[1]
    
    Arr = ProcessScan()
    CreateLog(DirName, Arr)

if __name__ == "__main__":
    main()