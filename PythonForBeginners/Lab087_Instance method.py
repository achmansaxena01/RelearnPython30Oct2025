class Product:
    def __init__(self): #This is default constructor
        self.name = "Iphone"
        self.description = "Its Awsome"
        self.price = 700

    def __del__(self):
        print("Inside the destructor \n")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)
        print("\n")

p1 = Product()
p1.display()
p1 = None

p2 = Product()
p2.display()
p2 = None
