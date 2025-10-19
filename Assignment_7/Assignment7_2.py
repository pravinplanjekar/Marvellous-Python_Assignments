"""
Accept a list of integers from the user and use the map() function to double each
value.
Expected Input:
Enter list: 1 2 3 4 5
Expected Output:
Doubled list: [2, 4, 6, 8, 10]
"""

Double = lambda iNo : iNo * 2

def main():
    print("Enter the no of elements : "
    )
    iLength = int(input())

    Data = []

    print("Enter the elements : ")

    for no in range(iLength):
        no  = int(input())
        Data.append(no)

    MData = list(map(Double,Data))
    print(f"Doubled Lis : {MData}")


if __name__ == "__main__":
    main()
