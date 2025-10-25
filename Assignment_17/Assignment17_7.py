""" 7. Schedule a function that performs file backup every hour and writes a log entry
into backup_log.txt. """

import schedule
import time
import datetime
import shutil
import os


SOURCE_FILE = "Data.txt"          
BACKUP_FOLDER = "Backup_Folder"
LOG_FILE = "Backup_Log.txt"

def BackupFile():
    
    os.makedirs(BACKUP_FOLDER, exist_ok = True)

    TimeStamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    BackupPath = os.path.join(BACKUP_FOLDER, f"Backup_{TimeStamp}.txt")

    shutil.copy(SOURCE_FILE, BackupPath)

    
    fobj= open(LOG_FILE, "a")
    fobj.write(f"Backup created at {TimeStamp} \n")

    print(f"[✔] Backup successful at {TimeStamp}")

def main():
    print("Backup scheduler started...")

    schedule.every(1).minute.do(BackupFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
