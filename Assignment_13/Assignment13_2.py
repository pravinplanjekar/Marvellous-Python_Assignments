""" 2. Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects. """

class BankAccount:
    ROI = 10.5

    def __init__(self):
        print("Enter your name: ")
        self.Name = input()

        print("Enter the Ammount: ")
        self.Ammount = int(input())

    def Deposit(self):
        print("Enter the ammount that you want to deposit : ")
        Ammount = int(input())
        self.Ammount = self.Ammount + Ammount

    def Withdraw(self):
        print("Enter the ammount that you want to withdraw : ")
        Ammount = int(input())
        if(self.Ammount > Ammount):
            self.Ammount = self.Ammount - Ammount
        else:
            print("Insufficient funds")

    def CalculateInterest(self):
        self.Interest = self.Ammount * BankAccount.ROI/100

    def Display(self):
        print("Ammount in the bank account is : ",self.Ammount)
        print("Interest received from the bank is : ",self.Interest)
        print("------------------------------------------------")


def main():
    obj1 = BankAccount()

    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

if __name__ == "__main__":
    main()