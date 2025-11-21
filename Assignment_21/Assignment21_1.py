""" 1.Design automation script which display information of running processes as its name, PID,
Username.
Usage : ProcInfo.py"""
    
import psutil

def ProcessDisplay():
    Border = "*"*25
    print(Border)
    print("Information of currently running processess : ")
    print(Border)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name', 'pid', 'username'])
        print(info)

def main():
    ProcessDisplay()

if __name__ == "__main__":
    main()