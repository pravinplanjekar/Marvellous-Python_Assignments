""" 9. Create a class Product with attributes name and price. Implement __eq__ method
to compare two products if they are equal in price. """

class Product:
    def __init__(self, name, price):
        self.Name = name
        self.Price = price
        
    def __eq__(self, new):
        if((self.Name == new.Name) and (self.Price == new.Price)):
            return True
        else:
            return False

def main():
    obj1 = Product("Pravin", 1500)
    obj2 = Product("Pravin", 1500)
    obj3 = Product("Nikhil", 2000)
    
    print(obj1 == obj2)
    print(obj1 == obj3)
       
if __name__ == "__main__":
    main()