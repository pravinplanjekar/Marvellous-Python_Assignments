""" 8. Write a script that simulates checking for email updates every 10 seconds. (Use a
print statement like “Checking mail...” instead of real email logic.) """

import schedule
import time
import datetime

def CheckMail():
    print("Checking mail...  Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("Mail Checking Program Started... )")

    schedule.every(10).seconds.do(CheckMail)

    while True:
        schedule.run_pending()
        time.sleep(1)  
    
if __name__ == "__main__":
    main()
