"""
6. Sum of First N Natural Numbers
Write a recursive function to calculate sum from 1 to n.
sum_n(5) → 15
"""
"""
def Sum_N(iNo):
    iSum = 0

    for no in range(1,iNo+1):
        iSum = iSum + no
    return iSum
"""
iSum = 0
def Sum_N(iNo):
    global iSum

    if(iNo < 0):
        iNo == -iNo

    if(iNo >=1):
        iSum += iNo
        iNo -= 1
        Sum_N(iNo)
    return iSum

def main():
    print("Enter the numbers : ")
    iNo = int(input())

    Ret = Sum_N(iNo)
    print(f"Sum of first {iNo} numbers is : {Ret}")

if __name__ == "__main__":
    main()