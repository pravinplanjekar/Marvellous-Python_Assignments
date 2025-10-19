"""
Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.
"""
import threading
import time

def DisplayEvenNumbers(iNo):
    iCount = 0
    for i in range(2, iNo+1, 2):
        iCount += 1

        if(iCount > 10):
            break

        print(i)

def DisplayOddNumbers(iNo):
    iCount = 0
    for i in range(1, iNo+1, 2):
        iCount += 1

        if(iCount > 10):
            break

        print(i)


def main():
    print("Demonstration of parallel execution")

    start_time = time.time()

    T1 = threading.Thread(target = DisplayEvenNumbers, args = (1000,))
    T2 = threading.Thread(target = DisplayOddNumbers, args= (1000,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    end_time = time.time()

    print("Time required for execution is :", end_time - start_time)
    

if __name__ == "__main__":
    main()