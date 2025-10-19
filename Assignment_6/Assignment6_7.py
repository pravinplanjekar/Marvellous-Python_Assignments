"""
Accept 5 numbers from the user. Find and print the largest number.
Expected Input:
Enter 5 numbers: 23 89 12 56 45
Expected Output:
Maximum number is: 89

"""

def Maximum(Brr):
    iMax = Brr[0]

    for no in Brr:
        if(no > iMax):
            iMax = no
    return iMax

def main():
    print("Enter the number of elements :")
    iLength = int(input())

    Data = []

    print("Enter the elements :")

    for i in range(iLength):
        no = int(input())
        Data.append(no)

    print(Data)

    iRet = Maximum(Data)

    print(f"Maximum Number is : {iRet}")


if __name__ == "__main__":
    main()