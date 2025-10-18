def DisplayFactorials(iNo
    iFact = 1

    for i in range(1,iNo+1):
        iFact = iFact * i
        

    return iFact


def main():
    print("Enter the number :")
    iValue = int(input())

    iRet = DisplayFactorials(no)

    print("Factorials of the numbers are : ",iRet)


if __name__ == "__main__":
    main()