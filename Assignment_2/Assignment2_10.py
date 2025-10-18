def CountDigits(No):
    iSum = 0
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum
  

def main():
    print("Enter the number : ")
    iValue = int(input())

    iRet = CountDigits(iValue)
    print("Addition of digits are : ",iRet)

if __name__ == "__main__":
    main()