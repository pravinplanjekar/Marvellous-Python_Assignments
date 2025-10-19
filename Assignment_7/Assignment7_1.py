"""
Write two lambda functions:
• One to calculate square of a number
• Another to calculate cube of a number
Expected Input:
Enter a number: 3
Expected Output:
Square: 9
Cube: 27
"""

CalculateSquare = lambda iNo: iNo **2
CalculateCube = lambda iNo: iNo **3

def main():
    print("Enter the number : ")
    iValue = int(input())

    iRet1 = CalculateSquare(iValue)
    print(f"Square : {iRet1}")

    iRet2 = CalculateCube(iValue)
    print(f"Cube  : {iRet2}")

if __name__ == "__main__":
    main()