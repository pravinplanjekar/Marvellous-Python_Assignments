"""
Even or Odd Number Check
Write a program to check whether the entered number is even or odd.
Expected Input:
Enter a number: 17
Expected Output:
17 is an odd number.
"""
def CheckEvenOdd(iNo):
    if(iNo % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter the number : ")
    Value = int(input())

    bRet = CheckEvenOdd(Value)
    
    if(bRet == True):
        print(f"{Value} is an even number")
    else:
        print(f"{Value} is an odd number")


if __name__ == "__main__":
    main()