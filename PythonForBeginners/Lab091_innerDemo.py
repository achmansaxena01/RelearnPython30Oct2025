class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number
        def start(self):
            print(f"Engine with engine Number {self.number} started."   )

C1 = Car("Ford", "Mustang", 2016)
E1 = C1.Engine(1234)
E1.start()