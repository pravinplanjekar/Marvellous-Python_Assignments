"""
5. Count Zeros in a Number (Recursively)
Write a recursive function to count how many zeros are in the given number.
count_zeros(1020300) → 4
"""
"""
def CountZeros(No):
    iCount = 0
    iDigit = 0
    for no in range(No):
        if(No != 0):
            iDigit = No % 10
            No = No // 10

            if(iDigit == 0):
                iCount += 1

    return iCount
"""
iDigit = 0
iCount = 0
def CountZeros(No):
    global iDigit
    global iCount
    if(No != 0):
        iDigit = No % 10
        No = No // 10

        if(iDigit == 0):
            iCount += 1
        CountZeros(No)
    return iCount

def main():
    print("Enter the number :")
    No = int(input())

    Ret = CountZeros(No)
    print(f"Zeros in the {No} are {Ret}")

if __name__ == "__main__":
    main()