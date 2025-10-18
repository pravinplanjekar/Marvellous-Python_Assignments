def Add(No1, No2):
    Ans = 0

    Ans = No1 + No2

    return Ans

print("Enter first Number : ")
value1 = int(input())

print("Enter second Number :")
value2 = int(input())

result = Add(value1, value2)
    
print(f"Addition of {value1} and {value2} is : {result}")

