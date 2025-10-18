"""
Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
"""

CalculatePower = lambda No : 2**No

print("Enter the number :")
Value = int(input())

Ret = CalculatePower(Value)

print(f" Power of two of {Value} is : {Ret}")