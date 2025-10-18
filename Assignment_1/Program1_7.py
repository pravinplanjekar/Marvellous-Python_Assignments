def Divisibleby5():
    print("Enter the number")
    No = int(input())

    if(No % 5 == 0):
        return True
    else:
        return False

bRet = 0

bRet = Divisibleby5()
print(bRet)
