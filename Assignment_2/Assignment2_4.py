def SumFactors(iNo):

    iSum = 0
    
    if(iNo < 0):
        iNo = -iNo
        
    for i in range(1, iNo):
        if(iNo % i == 0):
            iSum += i 

    return iSum

def main():
    print("Enter the number : ")
    Value = int(input())


    iRet = SumFactors(Value)

    print("Additions of its Factors is : ",iRet)


if __name__ == "__main__":
    main()