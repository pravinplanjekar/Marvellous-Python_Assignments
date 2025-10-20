""" Create a class Book with private attribute __price. Add methods to get and set the
price. Show encapsulation. """

class Book:
    def __init__(self,A):
        self.__Price = A

    def GetPrice(self):
        return self.__Price
    
    def SetPrice(self, NewPrice):
        if NewPrice > 0:
            self.__Price = NewPrice
        else:
            print("Invalid Price, please enter price greater than zero")

def main():
    obj1 = Book(500)

    obj1.GetPrice()
    print("Initial price of book is : ",obj1.GetPrice())

    obj1.SetPrice(600)
    print("Revised price of book is : ",obj1.GetPrice())


if __name__ == "__main__":
    main()