""" 
Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5) 
"""

def ChkPrime(Brr):
    print("InsideMarvellousNum")

    Crr = []
    while(len(Brr) != 0):
        for no in Brr(2, no//2):
            if(Brr[i] % no == 0):
                Crr.append(i)

    print(Crr)
    return Crr

        

    