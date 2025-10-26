""" 5. Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
Search “Marvellous” in Demo.txt """

import sys

def main():
    if(len(sys.argv) != 3):
        print("Insufficient arguments")
        return
    
    FileName = sys.argv[1]
    obj1 = open(FileName, "r")
    Data = obj1.read()
    
    String = sys.argv[2]
    
    Frequency = Data.count(String)
    print(f"Frequency of {String} in {FileName} is {Frequency}")
    
if __name__ == "__main__":
    main()
    