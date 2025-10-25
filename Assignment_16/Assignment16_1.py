""" 1. Write a Python program to create a text file named student.txt and write the
names of 5 students into it. """

import sys

def main():
    print("Enter the file name you want to create:")
    FileName = input()
    
    fobj = open(FileName, "w")
    
    try:
        print("Enter the number of students :")
        Length = int(input())
    except ValueError:
        print("Error, please enter valid input in number format")
        return
    
    Data = []
    
    for name in range(Length):
        print("Enter the name of students : ")
        name = input()
        Data.append(name)
        
    #print("Data Entered : ",Data)
    
    FinalData = "\n".join(Data)
    
    fobj.write(FinalData)
    
    fobj.close()

if __name__ == "__main__":
    main()