"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
def ChkPrime(iNo):
    bFlag = True

    if(iNo < 0):
        iNo = -iNo

    for i in range(2, (iNo//2) +1):
        if(iNo % i == 0):
            bFlag = False
            break

    if(bFlag == True):
        return iNo

Multiplication = lambda iNo : iNo * 2

def Maximum(Data):
    iMax = Data[0]

    for No in Data:
        if(No > iMax):
            iMax = No

    return iMax

def main():
    print("Enter the elements : ")
    iLength = int(input())

    Data = []

    print("Enter the elements : ")
    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    FData = list(filter(ChkPrime, Data))
    print("Filter output is : ", FData)

    MData = list(map(Multiplication, FData))
    print("Map output is : ", MData)

    RData = Maximum(MData)
    print("Reduce Output is : ", RData)

if __name__ == "__main__":
    main()