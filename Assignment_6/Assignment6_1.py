"""
Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum
of all even numbers from 1 to 100.
Expected Output:
Sum of even numbers between 1 to 100 is: 2550
"""

def CheckEvenSum(iNo):
    iSum = 0

    for i in range(1, iNo+1):
        if(i % 2 == 0):
            iSum += i 

    return iSum


def main():
    print("Enter the number : ")
    Value = int(input())

    iRet = CheckEvenSum(Value)
    print(f"Sum of even numbers between 1 to {Value} is : {iRet}")

if __name__ == "__main__":
    main()
