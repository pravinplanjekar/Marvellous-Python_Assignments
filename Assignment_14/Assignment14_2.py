""" 2. Write a class Rectangle with length and width. Add a method to compute area and
perimeter.
Area: 50, Perimeter: 30 """

class Rectangle:
    def __init__(self):
        self.Length = int(input("Enter the Length : "))
        self.Width = int(input("Enter the width : "))

    def AreaPerimeter(self):
        self.Area = print("Area : ",self.Length * self.Width, ",", end=" ")
        self.Perimeter = print("Perimeter :",(2*(self.Length + self.Width)))

def main():
    obj = Rectangle()

    obj.AreaPerimeter()

if __name__ == "__main__":
    main()