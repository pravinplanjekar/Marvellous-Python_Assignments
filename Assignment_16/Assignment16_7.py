""" 7. Create a file marks.txt with student name and marks. Then read the file and
display students who scored more than 75 marks. """

import os 

def main():
    print("Enter the file name in which you want to store student's data : ")
    FileName = input()
    
    Flag = os.path.exists(FileName)
    
    if(Flag == True):
        print("File with same name is already present in the Directory.")
    else:
        print("File sucessfully created.")
        
        
    print("Enter the total number of students : ")
    iTotal = int(input())
    
    StudentsData = {}
    
    fobj = open(FileName, "w")
    for i in range(iTotal):
        Key = input("Enter the key : ")
        Value = int(input("Enter the value :"))
        StudentsData[Key] = Value
        fData = fobj.write(f"{Key} : {Value} \n")
        
    print("Data has been written sucessfully.")
    
    DStudents = []
    for Key, Value in StudentsData.items():
        if(Value > 75):
            DStudents.append(Key)
            
    print("Name of the students who scored above 75% are :")
    for name in DStudents:
        print(name)
        
    fobj.close()

if __name__ == "__main__":
    main()