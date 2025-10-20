""" 10. Demonstrate private, protected and public access modifiers using a class Employee
with attributes: __salary, _department, name. """

class Employee:
    def __init__(self, name, _department, __salary):
        self.Name = name 
        self._Department = _department 
        self.__Salary = __salary 
        
    def display(self):
        print(f"Name : {self.Name} , Department : {self._Department} , Salary : {self.__Salary}")

def main():
    obj1 = Employee("Pravin","Developer",100000)
    obj1.display()
    
    print(obj1.Name)
    print(obj1._Department)
    #print(obj1.__Salary)

if __name__ == "__main__":
    main()