"""
Write a function that accepts a string and checks whether it is a palindrome.
Expected Input:
Enter a string: radar

Expected Output:
radar is a palindrome.
"""

def CheckPallindrome(str):
    
    Rstr = ""

    for ch in str:
        Rstr = ch + Rstr
   
    if(str == Rstr):
        return True
   
def main():
    print("Enter String : ")
    str = input()

    sRet = CheckPallindrome(str)

    if(sRet ==True):
        print(f"{str} is Pallindrome")
    else:
        print(f"{str} is  not Pallindrome")

if __name__ == "__main__":
    main()

