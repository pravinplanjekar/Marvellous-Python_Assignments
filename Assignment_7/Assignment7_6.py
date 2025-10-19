"""
Write a function that accepts a list of integers and returns a list of prime numbers
using filter().
Expected Input:
Enter list: 10 11 12 13 14 15 16 17
Expected Output:
Prime numbers: [11, 13, 17]
"""

def CheckPrime(iNo):
    bFlag = True

    for no in range(2, (iNo // 2)+1):
        if(iNo % no == 0):
            bFlag = False

    if(bFlag == True):
        return iNo

def main():
    print("Enter the no of elements : ")
    iLength = int(input())

    Data = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)



    FData = list(filter(CheckPrime, Data))
    print(f"Prime Numbers : {FData}")


if __name__ == "__main__":
    main()