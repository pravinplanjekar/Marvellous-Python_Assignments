""" 6. Write a script that schedules multiple tasks: one to print "Lunch Time!" at 1 PM,
and another to print "Wrap up work" at 6 PM. """

import schedule
import time
import datetime

def ScheduleTask1():
    print("Lunch time!")  
    
def ScheduleTask6():
    print("Wrap up Work")  

def main():
    
    schedule.every().day.at("13:00").do(ScheduleTask1)
    schedule.every().day.at("17:00").do(ScheduleTask6)
    
    
    while(True):
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()