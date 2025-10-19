"""
Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.
"""
import threading
import time
import os

def DisplaySmall(Data):
    print("PID of small thread is : ", os.getpid())
    print("Small characters are : ")

    for no in Data:
        #if(no.islower()):
        if(no >= 'a' and no <= 'z'):
            print(no)

def DisplayCapital(Data):
    print("PID of capital thread is : ", os.getpid())
    print("Capital characters are : ")

    for no in Data:
        #if(no.isupper()):
        if(no >= 'A' and no <= 'Z'):
            print(no)

def DisplayDigits(Data):
    print("PID of digits thread is ", os.getpid())
    print("NUmbers are : ")
    
    for no in Data:
        #if(no.isdigit()):
        if(no >= '0' and no <= '9'):
            print(no)

def main():
    print("PID of the main thread is : ", os.getpid())
    print("Enter the string :")
    Str = input()

    start_time = time.time()

    small = threading.Thread(target = DisplaySmall, args = (Str,))
    capital = threading.Thread(target = DisplayCapital, args = (Str,))
    digits = threading.Thread(target = DisplayDigits, args = (Str,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    end_time = time.time()

    print("Process executon time is : ", end_time - start_time)
    

if __name__ == "__main__":
    main()