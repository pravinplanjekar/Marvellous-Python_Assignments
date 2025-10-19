"""
2. Factorial Using Recursion
Write a recursive function to calculate factorial of a number.
factorial(5) → 120
"""
"""
def Factorial(iNo):
    Fact = 1
    for no in range(1, iNo + 1):
        Fact *= no

    return Fact
"""

Fact = 1

def Factorial(iNo):
    global Fact

    if(iNo >= 1):
        Fact *= iNo
        iNo -= 1
        Factorial(iNo)

    return Fact

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Factorial(Value)
    print(f"Factorial of {Value} is {Ret}")

if __name__ == "__main__":
    main()
