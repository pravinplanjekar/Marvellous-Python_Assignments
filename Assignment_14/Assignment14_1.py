""" 1. Create a class Employee with attributes name, emp_id, and salary. Create objects
of this class and print their details using a method.
Expected Output:
Name: Rohit, ID: 101, Salary: 50000 """
class Employee:
    def __init__(self,A,B,C):
        self.Name = A
        self.Emp_id = B
        self.Salary = C

    def DisplayInfo(self):
        print(self.Name,",", self.Emp_id,",", self.Salary)
        

def main():

    obj1 = Employee("Pravin","ID: AB123",50000)
    obj1.DisplayInfo()
    print("---------------------------------------------")

    obj2 = Employee("Abhilasha","ID: AB321",25000)
    obj2.DisplayInfo()


if __name__ == "__main__":
    main()