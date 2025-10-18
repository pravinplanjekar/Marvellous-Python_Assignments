"""
Voting Eligibility Checker
Accept age from the user and check whether the person is eligible to vote. (Age should be
18 or above.)
Expected Input:
Enter age: 19
Expected Output:
Eligible to vote.
"""

def VotingEligibilityChecker(iNo):
    if(iNo >= 18):
        return True
   

def main():
    print("Enter the Age : ")
    Value = int(input())

    iRet = VotingEligibilityChecker(Value)

    if(iRet == True):
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")
   

if __name__ == "__main__":
    main()