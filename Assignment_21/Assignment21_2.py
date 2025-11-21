""" 2.Design automation script which accept process name and display information of that process if
it is running.
Usage : ProcInfo.py Notepad """

import psutil

def ProcInfo(Name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == Name:
            print(f"{Name} is running in the system")
            exit()
            
    print("No susch process is running in the system")
        
               
def main():
    ProcInfo("Notepad.exe")

if __name__ == "__main__":
    main()