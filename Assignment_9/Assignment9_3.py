"""3. Create a Python program that uses multiprocessing.Pool to compute
factorial of numbers in a list."""

import os
import time
import multiprocessing

def Factorial(No):
    print("PID is : ",os.getpid())

    Fact = 1
    for no in range(1,No+1):
            Fact = Fact * no
            #no +=1
    return Fact

def main():
    start_time = time.time()

    print("Enter the elements:")
    iLength = int(input())

    Data = []

    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    result = []

    p = multiprocessing.Pool()
    result = p.map(Factorial,Data)

    p.close()
    p.join()

    print(result)

    end_time = time.time()

    print("Execution time is :",end_time - start_time)

if __name__ == "__main__":
    main()