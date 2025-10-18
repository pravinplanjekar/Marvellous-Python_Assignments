def DisplayEvenNumbers():
    print("Enter the number :")
    No = int(input())

    for i in range(2, No*2+2):
        if(i % 2 == 0):
            print(i)

DisplayEvenNumbers()