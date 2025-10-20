""" 4. Create a class Student with name, roll_no, and a class variable school_name. Print
student details and school name. Change the school name using class name. """

class Student:
    SchoolName = "PUMBA"

    def __init__(self, A, B):
        self.Name = A
        self.RollNo = B 
        
    def DisplayInfo(self):
        print("School name is : ",Student.SchoolName) 
        print("name of the student is : ",self.Name)
        print("Roll No of the student is : ", self.RollNo)
        print("-----------------------------------------------")

def main():
    obj1 = Student("Pravin",23)

    obj1.DisplayInfo()

    Student.SchoolName = "SPPU"

    print("Student details  after changng School name : ")
    obj1.DisplayInfo()  


if __name__ == "__main__":
    main()