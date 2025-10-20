""" 7. Create a base class Person with name and age. Derive a class Teacher with subject
and salary. Use super() to call base class constructor and print both. """

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        print("Inside Person Constructor...")
        
    def DisplayPerson(self):
        print(f"Name : {self.Name} , Age : {self.Age}")
        
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.Subject = subject
        self.Salary = salary 
        print("Inside Teacher Constructor...")
        
        
    def DisplayTeacher(self):
        print(f"Subject : {self.Subject} , Salaey : {self.Salary}")
        
def main():
    obj1 = Teacher("Pravin",34,"Python Programming",50000)
    
    obj1.DisplayPerson()
    obj1.DisplayTeacher()

if __name__ == "__main__":
    main()