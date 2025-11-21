""" 4. Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.
Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id. """

import psutil
import os
import time
import sys
import smtplib
from email.message import EmailMessage

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

def MailLogReport(SenderEmail, SenderPassword, ReceiverEmail, Subject, Body, FilePath):
    Msg = EmailMessage()
    
    Msg["From"] = SenderEmail
    Msg["To"] = ReceiverEmail
    Msg["Subject"] = Subject
    Msg.set_content(Body)
    
    if os.path.exists(FilePath):
        fobj = open(FilePath, "rb")
        FileData = fobj.read()
        FileName = os.path.basename(FilePath)
        Msg.add_attachment(FileData, maintype = "application", subtype = "octet-stream", filename = FileName)
        print(f"File attached : {FileName}")
    else:
        print("File not found...")
        return
    
    try:
        Server = smtplib.SMTP("smtp.gmail.com", 587)
        Server.starttls()
        Server.login(SenderEmail, SenderPassword)
        Server.send_message(Msg)
        print("Email sent Sucessfully.")
    except Exception as eobj:
        print("Error sending email:", eobj) 
        
        fobj.close()
        Server.close()

def main():
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h"):
            print("This application is used to create a long of running processes")
            return
        
        if(sys.argv[1] == "--u"):
            print("Execute the code as : ")
            print("python Filename.py Directory Name Email id")
            return

    if(len(sys.argv) != 3):
        print("Insufficient number of arguments")
        print("You can use --h for help as --u for usage")
        return
    
    DirName = sys.argv[1]
    EmailID = sys.argv[2]
    
    Arr = ProcessScan()
    CreateLog(DirName, Arr)
    
    SenderEmail = "piyu042025@gmail.com"
    SenderPassword = "xyfe havv hxcx tjuq"
    ReceiverEmail = EmailID
    Subject = "System process Log File."
    Body = "Hello Sir, \n\nPlease find attached the process log file report.\n\nRegards,\nPravin"
    FilePath = r"C:\Users\pravi\OneDrive\Desktop\Marvellous\Python\Assignments\Automation_Assignment_21\Demo\MarvellousSatNov818_21_432025.log"

    MailLogReport(SenderEmail, SenderPassword, ReceiverEmail, Subject, Body, FilePath)

if __name__ == "__main__":
    main()