"""
Write a program to accept two integers from the user and display their:
• Sum
• Difference
• Product
• Division
Expected Input:
Enter first number: 10
Enter second number: 2
Expected Output:
Sum: 12
Difference: 8
Product: 20
Division: 5.0
"""

Sum = lambda No1, No2 : No1 + No2

Difference = lambda No1, No2 : No1 - No2

Product = lambda No1, No2 : No1 * No2

Division  = lambda No1, No2 : No1 // No2


def main():
    print("Enter first number : ")
    Value1 = float(input())

    print("Enter second number : ")
    Value2 = float(input())

    iRet1 = Sum(Value1, Value2)
    iRet2 = Difference(Value1, Value2)
    iRet3 = Product(Value1, Value2)
    iRet4 = Division(Value1, Value2)

    print("Sum of the numbers is : ", iRet1)
    print("Difference of the numbers is : ", iRet2)
    print("Product of the numbers is : ", iRet3)
    print("Division of the numbers is : ", iRet4)

if __name__ == "__main__":
    main()