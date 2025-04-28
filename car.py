class Car:
    def __init__(self, make, model, year, num_doors, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.mileage = mileage

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model} with {self.num_doors} doors.")
        print(f"Current mileage: {self.mileage} km\n")

    def update_mileage(self, km):
        self.mileage += km