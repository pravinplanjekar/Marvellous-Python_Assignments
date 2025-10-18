""" Write a program which accept N numbers from user and store it into List. Return Minimum
    number from that List."""

def Minimum(Brr):
    iMin = Brr[0]

    for no in Brr:
        if(no < iMin):
            iMin = no

    return iMin
    

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    iRet = Minimum(Arr)
    print(f"Minimum numbers is : {iRet}")

if __name__ == "__main__":
    main()