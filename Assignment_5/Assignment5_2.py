"""
Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
print it's a consonant.
Expected Input:
Enter a character: e
Expected Output:
'e' is a vowel.
"""

def CheckVowel(Ch):
    if(Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u' ):
        return True
   

def main():
    print("Enter the character : ")
    Char = input()

    cRet = CheckVowel(Char)

    if(cRet == True):
        print("Character is Vowel")
    else:
        print("Character is Consonant")


if __name__ == "__main__":
    main()