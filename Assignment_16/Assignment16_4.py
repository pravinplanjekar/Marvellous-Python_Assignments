""" 4. Accept 10 numbers from the user and write them into a file named numbers.txt,
each on a new line. """

import sys

def main():
    print("Enter the file name you want to create:")
    FileName = input()
    
    fobj = open(FileName, "w")
    
    try:
        print("Enter the total count of numbers :")
        Length = int(input())
    except ValueError:
        print("Error, please enter valid input in number format")
        return
    
    Data = []
    
    for no in range(Length):
        print("Enter the numbers : ")
        no = int(input())
        Data.append(no)
        
    #print("Data Entered : ",Data)
    
    DataNumber = map(str, Data)
    FinalData = "\n".join(DataNumber)
    
    fobj.write(FinalData)
    print("Numbers are written in the file sucessfully.")
    
    fobj.close()

if __name__ == "__main__":
    main()