def DisplayPattern(Value):

    for i in range(Value):
        for j in range(Value):
            print("*",end= "  ")

        print()


def  main():
    print("Enter the number : ")
    no = int(input())


    DisplayPattern(no)

if __name__ == "__main__":
    main()