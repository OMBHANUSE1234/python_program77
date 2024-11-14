class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"{self.make} {self.model} ({self.year}) created.")


    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Manufacturing Year: {self.year}")


    def __del__(self):
        print(f"{self.make} {self.model} ({self.year}) destroyed.")


my_car = Car("Toyota", "Camry", 2020)  # Constructor is called

my_car.display_info()


del my_car
