import Arithmetic as A

print("Enter first number : ")
no1 = int(input())

print("Enter second number : ")
no2 = int(input())

Ans = A. Add(no1, no2)
print(" Addition is : ",Ans)

Ans = A.Sub(no1, no2)
print(" Substraction is : ",Ans)

Ans = A.Mult(no1, no2)
print(" Multiplication is : ",Ans)

Ans = A.Div(no1, no2)
print(" Division is : ",Ans)
