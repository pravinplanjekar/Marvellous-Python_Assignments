""" 2. Schedule a task that displays the current date and time every minute using the
datetime module. """

import schedule
import datetime
import time 

def main():
    
    print(f"Current date and time is : {datetime.datetime.now()}")

if __name__ == "__main__":
    main()