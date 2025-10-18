def CountDigits(No):
    Count = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Count = Count +1
        No = No // 10

    return Count
  

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = CountDigits(Value)
    print("Number of digits are : ",Ret)

if __name__ == "__main__":
    main()