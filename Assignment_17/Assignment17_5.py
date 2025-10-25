""" 5. Schedule a job that runs every 5 minutes to write the current time to a file
Marvellous.txt. """

import schedule
import time 
import datetime

FileName = "Marvellous.txt"

def WriteTime():
    
        TimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        fobj = open(FileName, "a")
        fobj.write(TimeStamp + "\n")
        
        print(f"TimeStamp : {TimeStamp}")
        
def main():
    
    fobj = open(FileName, "w")
    schedule.every(5).minutes.do(WriteTime)
    
    
    while True:
        schedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__":
    main() 
    
""" import schedule
import time
import datetime
import os

FILENAME = "Marvellous.txt"

def write_time():
    # Make a nice timestamp string
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Append to the file (creates it if it doesn't exist)
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(stamp + "\n")
    print(f"Wrote: {stamp}")

def main():
    # Ensure file exists with a header (optional)
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write("# Time log (every 5 minutes)\n")

    # Schedule the job every 5 minutes
    schedule.every(2).seconds.do(write_time)

    print("Scheduler started. Writing time to Marvellous.txt every 5 minutes. Press Ctrl+C to stop.")
    # Keep the scheduler running
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # prevent high CPU usage
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main() """
