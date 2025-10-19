"""
Print Triangle Pattern using Nested Loops
Expected Output:

*
* *
* * *
* * * *

"""

def DisplayPattern(iNo):
    for j in range(iNo):
        for i in range(iNo):
            if(i <= j):
                print("*",end="  ")
            
        print() 

def main():
    print("Enter the Row number : ")
    Value = int(input())

    DisplayPattern(Value)

if __name__ == "__main__":
    main()