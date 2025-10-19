"""
Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
"""

import threading
import time

def SumEvenFcators(iNo):
    iFact = 1
    iSum = 0

    for i in range(2,iNo + 1,2):
        if(iNo % i == 0):
            iFact = iFact * i
            iSum += i

    print("Addition of Even factors is :", iSum)

def SumOddFactors(iNo):
    iFact = 1
    iSum = 0

    for i in range(1, iNo + 1, 2):
        if(iNo % i == 0):
            iFact = iFact * i 
            iSum += i

    print("Addition of Odd factors is :", iSum)


def main():
    print("Enter the Number : ")
    Value = int(input())

    start_time = time.time()

    T1 = threading.Thread(target = SumEvenFcators, args = (Value,))
    T2 = threading.Thread(target = SumOddFactors, args = (Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Time required for the execution is : ", end_time - start_time)
if __name__ == "__main__":
    main()