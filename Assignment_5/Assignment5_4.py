"""
Find Largest Among Three Numbers
Accept three numbers from the user and print the largest using nested if-else statements.
Expected Input:
Enter three numbers: 5 9 3
Expected Output:
Largest number is 9.
"""
def Maximum(iNo1, iNo2, iNo3):
    iMax = iNo1
    if(iNo2 > iNo1):
        iMax = iNo2
    elif(iNo3 > iNo1):
        iMax = iNo3
    
    return iMax


def main():
    print("Enter first number :")
    Value1 = int(input())

    print("Enter first number :")
    Value2 = int(input())

    print("Enter first number :")
    Value3 = int(input())

    iRet = Maximum(Value1, Value2, Value3)
    print("Largest number is : ",iRet)

if __name__ == "__main__":
    main()