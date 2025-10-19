"""
1. Print Numbers Using Recursion
Write a recursive function to print numbers from 1 to N.
Expected Output (for n=5):
1 2 3 4 5
"""
"""
def DisplayNumbers(iNo):
    for no in range(1, iNo + 1):
        print(no, end=" ")
"""

i = 1

def DisplayNumbers(iNo):
    global i
    if(i <= iNo):
        print(i, end=" ")
        i += 1
        DisplayNumbers(iNo)

def main():
    print("Enter the number :")
    Value = int(input())

    DisplayNumbers(Value)

if __name__ == "__main__":
    main()