""" 5. Create a class BankAccount with account_number, name, and balance. Use
__init__ and create methods for deposit, withdraw, and displaying balance. """

class BankAccount:
    def __init__(self,account_number,name,balance):
        self.AccountNumber = account_number
        self.Name = name
        self.Balance = balance

    def Deposit(self):
        print("Enter the  deposit ammount :")
        Deposit = int(input())
        self.Balance += Deposit

        print("Total balance in the account after deposition is :",self.Balance)

    def Withdraw(self):
        print("Enter the withdrawal ammount :")
        withdraw_ammount = int(input())

        if(withdraw_ammount <= self.Balance):
            self.Balance -= withdraw_ammount
            print("Ammount withdrawn sucessfully")
            print("Bank Account Balance after withdrawal is :",self.Balance)
        else:
            print("Insufficient Balance")

    def DisplayBalance(self):
        print("------------------------------------------------------")
        print("Bank account number is : ", self.AccountNumber)
        print("Account holder name is :",self.Name)
        print("Current Balance in the account is : ",self.Balance)
        print("------------------------------------------------------")

def main():
    obj1 = BankAccount(543215,"Pravin",100000)
    obj1.DisplayBalance()

    obj1.Deposit()
    obj1.Withdraw()
    obj1.DisplayBalance()

if __name__ == "__main__":
    main()