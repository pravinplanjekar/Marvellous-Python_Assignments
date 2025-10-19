""" 3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects. """

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first number : ")
        self.Value1 = int(input())

        print("Enter the second number : ")
        self.Value2 = int(input())

    def Addition(self):
        Addition = self.Value1 + self.Value2
        return Addition
    
    
    def Substraction(self):
        Substraction = self.Value1 - self.Value2
        return Substraction
    
    def Multiplication(self):
        Multiplication = self.Value1 * self.Value2
        return Multiplication
    
    def Division(self):
        if self.Value2 != 0:
            Division = self.Value1 / self.Value2
            return Division
        else:
            return "Division by zero is wrong input, please provide non zero input"


def main():
    obj1 = Arithmetic()

    obj1.Accept()
    RetAdd = obj1.Addition()
    RetSub = obj1.Substraction()
    RetMult = obj1.Multiplication()
    RetDiv = obj1.Division()

    print(f"Addition is : {RetAdd} ")
    print(f"Substraction is : {RetSub}")
    print(f"Multiplicaion is : {RetMult}")
    print(f"Division is : {RetDiv}")
    print("----------------------------------------------")


    obj2 = Arithmetic()

    obj2.Accept()
    RetAdd = obj2.Addition()
    RetSub = obj2.Substraction()
    RetMult = obj2.Multiplication()
    RetDiv = obj2.Division()

    print(f"Addition is : {RetAdd} ")
    print(f"Substraction is : {RetSub}")
    print(f"Multiplicaion is : {RetMult}")
    print(f"Division is : {RetDiv}")

if __name__ == "__main__":
    main()