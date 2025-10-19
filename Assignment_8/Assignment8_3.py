"""
Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.
"""

import threading
import time

def EvenList(Data):
    iSum = 0

    for no in Data:
        if(no % 2 == 0):
            iSum += no
            print(iSum)

    print(f"Addition of even elements of the input is : {iSum}")

def Oddlist(Data):
    iSum = 0

    for no in Data:
        if(no % 2 != 0):
            iSum += no

    print(f"Addition of odd elements of the input is : {iSum}")


def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Data = []

    print("Enter the number of elements : ")

    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    start_time = time.time()

    T1 = threading.Thread(target = EvenList, args = (Data,))
    T2 = threading.Thread(target = Oddlist, args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Threads execution time is : ", end_time -  start_time)

    


if __name__ == "__main__":
    main()
