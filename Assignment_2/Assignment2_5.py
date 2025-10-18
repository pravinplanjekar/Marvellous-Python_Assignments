def DisplayPrimeNumbers(iNo):

    bFlag = True
    if(iNo < 0):
        iNo = -iNo
    
    for i in range(2, iNo):
        if(iNo % i == 0):
            bFlag = False
            
    return bFlag
    
        


def main():
    
    print("Enter the Number : ")
    Value = int(input())

    bRet = DisplayPrimeNumbers(Value)
    if(bRet == True):
        print(" Number is Prime Number")
    else:
        print("Number is not Prime Number")


if __name__ == "__main__":
    main()