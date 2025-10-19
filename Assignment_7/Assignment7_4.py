"""
Accept a list of numbers and use reduce() (from functools) to find the product of
all numbers.
Expected Input:
Enter list: 2 3 4
Expected Output:
Product: 24
"""
from functools import reduce

Product = lambda iNo1, iNo2 : iNo1 * iNo2

def main():
    print("Enter the no of elements : ")
    iLength = int(input())

    Data = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    RData = reduce(Product, Data)
    print(f"Product is : {RData}")

if __name__ == "__main__":
    main()