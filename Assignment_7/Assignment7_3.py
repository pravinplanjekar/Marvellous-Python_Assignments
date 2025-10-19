"""
Accept a list of numbers and use filter() to keep only even numbers.
Expected Input:
Enter list: 1 2 3 4 5 6
Expected Output:
Even numbers: [2, 4, 6]
"""

CheckEven = lambda iNo : iNo % 2 == 0


def main():
    print("Enter the no of elements : ")
    iLength = int(input())

    Data = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    fData = list(filter(CheckEven, Data))
    print(f" Even numbers : {fData}")

if __name__ == "__main__":
    main()
