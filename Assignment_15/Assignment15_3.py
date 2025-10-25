""" 3.Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt """

def main():
    print("Enter the file name that you want to create : ")
    FileName = input()
    
    fobj = open("ABC.txt","r")
    Data = fobj.read()
    
    fobj = open(FileName, "w")
    fobj.write(Data)
    
    fobj.close()

if __name__ == "__main__":
    main()