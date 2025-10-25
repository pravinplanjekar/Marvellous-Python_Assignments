""" 3. Write a Python script to count the number of lines, words, and characters in a
given file. """

import os
import sys

def CountLines(FileObj):
        Count = 0
    
        for lines in FileObj:
            Count += 1
        return Count
    
def CountWords(FileObj):
    Data = FileObj.read()
    """  Lines = Data.split()
    print(Lines) """
    Words = Data.split()
    #print(Words)
    return len(Words)

def CountChar(FileObj):
    Data = FileObj.read()
    CharCount = len(Data)
    return CharCount
    

def main():
    print("Enter the file name you want to read :")
    FileName = input()
    
    Ret = os.path.exists(FileName)
    
    if(Ret == True):
        print("file exists in the Directory.")
    else:
        print("There is no such file.")
        return
    
    fobj = open(FileName, "r")
    RetLines = CountLines(fobj)
    
    print(f"Number of lines present in the file {FileName} are : {RetLines}")
    
    fobj.seek(0)
    
    RetWords = CountWords(fobj)
    print(f"Number of words present in the file {FileName} are : {RetWords}")
    
    fobj.seek(0)
    
    RetChar = CountChar(fobj)
    print(f"Number of characters present in the file {FileName} are : {RetChar}")
        
    fobj.close()
    
if __name__ == "__main__":
    main()