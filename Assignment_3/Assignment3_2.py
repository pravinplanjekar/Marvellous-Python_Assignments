""" Write a program which accept N numbers from user and store it into List. Return Maximum
    number from that List."""

def Maximum(Brr):
    iMax = Brr[0]

    for no in Brr:
        if(no > iMax):
            iMax = no

    return iMax
    

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    iRet = Maximum(Arr)
    print(f"Maximum numbers is : {iRet}")

if __name__ == "__main__":
    main()