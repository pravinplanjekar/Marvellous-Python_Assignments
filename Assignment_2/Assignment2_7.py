def DisplayNumberMattrix(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j,end="  ")

        print()


def main():
    print("Enter the number :")
    Value = int(input())


    DisplayNumberMattrix(Value)


if __name__ == "__main__":
    main()