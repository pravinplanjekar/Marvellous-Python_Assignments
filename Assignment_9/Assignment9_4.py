"""4. Create a Python program that Compare execution time of summing
numbers from 1 to 10 million using normal function, threading, and
multiprocessing."""

import threading
import time
import multiprocessing

def Addition(Numbers):
    Sum = 0
    for no in range(1,len(Numbers)+1):
        Sum += no

    print(Sum)


def main():
    Numbers = list(range(1,1000001))
   # print(Numbers)
    start_time1 = time.time()

    Addition1 = Addition(Numbers)

    end_time1 = time.time()

    start_time2 = time.time()

    Addition2 = threading.Thread(target = Addition, args = (Numbers,))

    Addition2.start()
    Addition2.join()

    end_time2 = time.time()

    start_time3 = time.time()

    Addition3 = multiprocessing.Process(target = Addition, args = (Numbers,))

    Addition3.start()
    Addition3.join()

    end_time3 = time.time()

    print("Execution time with norma summing function is : ",end_time1 - start_time1)
    print("Execution time with threading summing function is : ",end_time2 - start_time2)
    print("Execution time with multiprocessing summing function is : ", end_time3 - start_time3)

if __name__ == "__main__":
    main()