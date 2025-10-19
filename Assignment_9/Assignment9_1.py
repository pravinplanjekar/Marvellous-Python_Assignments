"""Create a Python program that starts 3 threads, each printing numbers
from 1 to 5 with a delay of 1 second. Use threading.Thread.
"""

import threading
import time
#import schedule

def DisplayNumbers(iNo):
    for no in range(iNo+1):
        print(no, end=" ")

    print()

def main():
    print("Enter the number : ")
    iNo = int(input()) 

    T1 = threading.Thread(target = DisplayNumbers, args = (iNo,))
    T1.start()

    time.sleep(1)

    T2 = threading.Thread(target = DisplayNumbers, args = (iNo,))
    T2.start()

    time.sleep(1)

    T3 = threading.Thread(target = DisplayNumbers, args = (iNo,))
    T3.start()


if __name__ == "__main__":
    main()
    
