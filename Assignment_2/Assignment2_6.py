def DisplayPattern(No):

    for Col in range(1, No+1):
        for Row in range(1, No+1):
            if(Col <= Row):
                print("*",end = "  ")

        print()


def main():
    print("Enter the number : ")
    Value = int(input())

    DisplayPattern(Value)

if __name__ == "__main__":
    main()