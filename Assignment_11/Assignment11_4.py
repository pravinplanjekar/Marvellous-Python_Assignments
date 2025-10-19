"""
4. Power Function Using Recursion
Write a recursive function to calculate x^n.
power(2, 3) → 8
"""
"""
def CalculatePower(No1, No2):

    if(No2 < 0):
        {
            No2 == - No2
        }

    Power = 1
    for no in range(No2):
        Power = Power * No1 
        
    return Power
"""
Power = 1
def CalculatePower(No1, No2):
    global Power

    if(No2 < 0):
        No2 == - No2

    if(No2 >= 1):
        Power = Power * No1
        No2 -= 1
        CalculatePower(No1, No2)

    return Power

def main():
    print("Enter the  base number : ")
    No1 = int(input())

    print("Enter the power number :")
    No2 = int(input())

    Result = CalculatePower(No1, No2)
    print(f"{No2} th power of {No1} is : {Result}")

if __name__ == "__main__":
    main()
