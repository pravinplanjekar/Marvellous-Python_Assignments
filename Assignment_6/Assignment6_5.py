"""
Accept a number from the user and check whether it is prime or not.
Expected Input:
Enter a number: 11
Expected Output:
11 is a prime number.
"""

def CheckPrime(iNo):
    bFlag = True

    for i in range(2, (iNo//2)+1):
        if(iNo % i == 0):
            bFlag = False

    return bFlag

def main():
    print("Enter the number : ")
    Value = int(input())

    iRet = CheckPrime(Value)

    if(iRet == True):
        print(f"{Value} is a prime number.")
    else:
        print(f"{Value} is not a prime number.")


if __name__ == "__main__":
    main()

