""" 6. Create a class Calculator with methods for add, subtract, multiply, divide. Ask user
input for values and call methods accordingly. """

class Calculator:
    def __init__(self):
        self.Length = int(input("Enter the number of elements :"))

        self.Numbers = []
        for no in range(self.Length):
            no = int(input())
            self.Numbers.append(no)

        print(self.Numbers)

    def Add(self):
        self.Sum = 0
        for no in self.Numbers:
            self.Sum += no
        return self.Sum

    def Subtract(self):
        self.Sub = self.Numbers[0]

        for no in self.Numbers[1:]:
            self.Sub -= no
        return self.Sub

    def Multiply(self):
        self.Mul = self.Numbers[0]
        for no in self.Numbers[1:]:
            self.Mul *= no
        return self.Mul

    def Divide(self):
        self.Div = self.Numbers[0]
        for no in self.Numbers[1:]:
            self.Div /= no
        return self.Div       

def main():
    obj1 = Calculator()

    RetAdd = obj1.Add()
    print(f"Addition of given numbers  is : {RetAdd}")

    RetSub = obj1.Subtract()
    print(f"Subtraction of given numbers is : {RetSub}")
    
    RetMul = obj1.Multiply()
    print(f"Multiplication of given numbers is : {RetMul}")
    
    RetDiv = obj1.Divide()
    print(f"Division of given numbers is : {RetDiv}")

if __name__ == "__main__":
    main()