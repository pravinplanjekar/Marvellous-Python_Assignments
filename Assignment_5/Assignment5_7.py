"""
Area and Perimeter of Rectangle
Accept the length and width of a rectangle. Calculate and display the area and perimeter.
Expected Input:
Enter length: 5
Enter width: 3
Expected Output:
Area: 15
Perimeter: 16
"""

#def CalculateAreaPerimeter(fLen, fWidth):
Area = lambda iLen, iWidth : iLen * iWidth
    
Perimeter = lambda iLen, iWidth: 2*(iLen + iWidth)

def main():
    print("Enter length : ")
    Value1 = int(input())

    print("Enter width : ")
    Value2 = int(input())

    iRet1 = Area(Value1,Value2)
    print(f"Area : {iRet1}")

    iRet2 = Perimeter(Value1,Value2)
    print(f"Perimeter is : {iRet2}")


if __name__ == "__main__":
    main()
