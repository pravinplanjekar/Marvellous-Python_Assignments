""" 1.Write a program which contains one class named as Demo.
Demo class contains two instance variables as no1 ,no2.
That class contains one class variable as Value.
There are two instance methods of class as Fun and Gun which displays values of instance
variables.
Initialise instance variable in init method by accepting the values from user.
After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun() """

class Demo:
    Value = 10

    def __init__(self, No1, No2):
        self.A = No1
        self.B = No2

    def Fun(self):
        print("Inside Fun Method")
        print("value of No1 is : ", self.A)
        print("Value of No2 is : ", self.B)
        print("value of Class variable Value is : ", Demo.Value)
        print("--------------------------------------------")

    def Gun(self):
        print("Inside Gun Method")
        print("value of No1 is : ", self.A)
        print("Value of No2 is : ", self.B)
        print("value of Class variable Value is : ", Demo.Value)
        print("--------------------------------------------")

def main():
    
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()

