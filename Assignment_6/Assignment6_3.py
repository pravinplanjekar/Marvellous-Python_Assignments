"""
Accept a number from the user and print its multiplication table up to 10.
Expected Input:
Enter a number: 7
Expected Output
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""

def MultiplicationTable(iNo):
    iFact = 1
    
    for i in range(1, 11):
        iFact = i * iNo

        print(f"{i} x 7 = {iFact}")

   # return iFact


def main():
    print("Enter the number : ")
    Value = int(input())

    iRet = MultiplicationTable(Value)
   # print(f"Multiplication table of {Value} is : {iRet}")


if __name__ == "__main__":
    main()