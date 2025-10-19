"""
Write a Python program using multiprocessing.Process to square a list of
numbers using multiple processes.
"""

import os
import multiprocessing
import time

def Square(Arr):
    #print(Arr)

    Sq = []
    for no in Arr:
        no = no**2
        Sq.append(no)

    print(Sq)   

def main():
    print("PID of main process is :", os.getpid())

    print("Enter the number of elements :")
    iLength = int(input())

    Arr = []
    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    print(Arr)

    start_time = time.time()

    T1 = multiprocessing.Process(target=Square, args=(Arr,))

    T1.start()

    T1.join()

    end_time = time.time()

    print("Time required for the execution is : ",end_time - start_time)
     
if __name__ == "__main__":
    main()