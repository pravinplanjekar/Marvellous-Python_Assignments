""" 
Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5) 
"""
import MarvellousNum as Mv

def ListPrime():
    pass
    

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Enter the elements")

    for no in range(iLength):
        no = int(input())
        Arr.append(no)

    print(Arr)

    Ans = Mv.ChkPrime(Arr)
    print(f"List of prime numbers is : {Ans}")
    


if __name__ == "__main__":
    main()