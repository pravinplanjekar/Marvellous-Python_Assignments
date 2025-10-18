""" Problem Statement : Write a program which accept N numbers from user and store it into List. Return addition of all
    elements from that List."""

def Addition(Brr):
    iSum = 0

    for no in Brr:
        iSum += no

    return iSum

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    iRet = Addition(Arr)
    print(f"Addition  of the numbers is : {iRet}")

if __name__ == "__main__":
    main()