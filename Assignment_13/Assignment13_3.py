""" 3. Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects. """

class Arithmetic:
    def __init__(self):
        self.Value = int(input("Enter the number : "))
        
    def ChkPrime(self):
        self.BFlag =  True
        for no in range(2,self.Value):
            if(self.Value % no == 0 ):
                self.BFlag = False

        print("Number is prime : ",self.BFlag)        

    def Chkperfect(self):
       
        self.Sum = 0
        for no in range(1,self.Value):
            if(self.Value % no == 0):
                self.Sum += no

        if(self.Value == self.Sum):
            print("Number is Perfect number : ",True)
        else:
            print("Number is Perfect number : ",False)

    def Factors(self):
        self.Factors = []
        for no in range(1, self.Value):
           if(self.Value % no == 0):
                self.Factors.append(no)
                
        print(f"factors of {self.Value} are : {self.Factors}")

    def SumFactors(self):
        self.Sum = 0
        for no in range(1, self.Value):
           if(self.Value % no == 0):
               self.Sum += no

        print(f"Summation of factors of {self.Value} is {self.Sum}")      
        
def main():
    obj1 = Arithmetic()

    obj1.ChkPrime()
    obj1.Chkperfect()
    obj1.Factors()
    obj1.SumFactors()
    
if __name__ == "__main__":
    main()