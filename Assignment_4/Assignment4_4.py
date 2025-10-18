"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""

from functools import reduce

ChkEven = lambda No : No % 2 == 0
Square = lambda No : No ** 2
Sum = lambda No1, No2 : No1 + No2

def main():
    print("Enter the number of elements :")
    iLength = int(input())

    Data = []

    print("Enter the elements :")
    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    FData = list(filter(ChkEven, Data))
    print("Filter output is : ", FData)

    MData = list(map(Square, FData))
    print("Map output is : ", MData)

    RData = reduce(Sum,MData)
    print("Reduce output is", RData)
    

if __name__ == "__main__":
    main()