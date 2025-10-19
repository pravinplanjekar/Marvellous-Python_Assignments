"""
Accept a number and print its factorial using a for loop.
Expected Input:
Enter a number: 5
Expected Output:
Factorial of 5 is: 120
"""

def Factorial(iNo):
    iFact = 1

    for i in range(1,iNo+1):
        iFact *= i 

    return iFact 


def main():
    print("Enter the number : ")
    Value = int(input())

    iRet = Factorial(Value)
    print(f"Factorial of {Value} is : {iRet}")

if __name__ == "__main__":
    main()