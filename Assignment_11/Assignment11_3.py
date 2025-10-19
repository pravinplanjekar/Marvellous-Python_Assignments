"""
3. Sum of Digits
Write a recursive function to calculate the sum of digits of a number.
sum_of_digits(1234) → 10
"""
"""
def SumOfDigits(iNo):
    iDigit = 0
    iSum = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo//10
    return iSum
"""
iDigit = 0
iSum = 0
def SumOfDigits(iNo):
    global iDigit
    global iSum
    if(iNo != 0):
        iDigit = iNo % 10
        iSum += iDigit
        iNo //= 10
        SumOfDigits(iNo)
    return iSum 


def main():
    print("Enter the number of digits : ")
    No = int(input())

    iRet = SumOfDigits(No)
    print(f"Sum of digits of {No} is {iRet}")

if __name__ == "__main__":
    main()
