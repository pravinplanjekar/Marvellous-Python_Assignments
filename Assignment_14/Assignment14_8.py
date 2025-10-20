""" 8. Create a class Vehicle with method start(). Derive class Car and override the
method start() with additional behavior. Show method overriding. """

class Vehicle:
    def start(self):
        print("This is Vehicle class method...")
        
class Car(Vehicle):
    def start(self):
        super().start()
        print("This is Car class method...")
        
        

def main():
    objC = Car()
      
    objC.start()
    

if __name__ == "__main__":
    main()