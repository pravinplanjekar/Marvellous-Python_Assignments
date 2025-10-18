"""
Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
"""

CalculateMultiplication = lambda No1 , No2 : No1 * No2

print("Enter the first  number :")
Value1 = int(input())

print("Enter the second number :")
Value2 = int(input())

Ret = CalculateMultiplication(Value1, Value2)

print(f" Multiplication  of {Value1} ans { Value2} is : {Ret}")