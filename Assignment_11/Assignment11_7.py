"""
7. Print Pattern Using Recursion (Right Triangle)
Write a recursive function to print the following pattern:
*
* *
* * *
* * * *
"""
def DisplayTrianglePttern(iRow, iCol):

    for j in range(iCol):
        for i in range(iRow):
            if(i <= j):
                print("*", end=" ")
            else:
                print("", end =" ")
        print()

def main():
    print("Enter the number of rows:")
    iRow = int(input())

    print("Enter the number of columns ")
    iCol = int(input())

    DisplayTrianglePttern(iRow, iCol)
    

if __name__ == "__main__":
    main()