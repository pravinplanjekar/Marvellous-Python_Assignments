""" Write a program which accept N numbers from user and store it into List. 
    Accept one another number from user and return frequency of that number from List."""

def NumberFrequency(Brr, No):
    iCount = 0

    for i in range(len(Brr)):
        if(Brr[i] == No):
            iCount += 1

    return iCount    
    

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Enter the elements : ")

    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    print("Enter the number for which you want to check the frequency : ")
    iValue = int(input())

    iRet = NumberFrequency(Arr,iValue)

    
    print(f"Frequency of {iValue} numbers is : {iRet}")

if __name__ == "__main__":
    main()