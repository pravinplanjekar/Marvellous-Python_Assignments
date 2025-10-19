"""
Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.
"""
import threading


def DisplayForwardNumbers(iNo):

    for i in range(1, iNo + 1):
        print(i)

def DisplayReverseNumbers(iNo):
    
    for i in range(iNo, 0, -1):
        print(i)

def main():
    print("Enter the number : ")
    iNo = int(input())

    T1 = threading.Thread(target = DisplayForwardNumbers, args = (iNo,))
    T2 = threading.Thread(target = DisplayReverseNumbers, args = (iNo,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()



if __name__ == "__main__":
    main()