class Vehicle:
    def __init__(self, manufacturing_date, color):
        self.manufacturing_date = manufacturing_date
        self.color = color


class Car(Vehicle):
    def __init__(self, manufacturing_date, color, brand):
        # super().__init__(manufacturing_date, color) // Call the parent class constructor
        self.manufacturing_date = manufacturing_date
        self.color = color
        self.brand = brand

    def display(self):
        print(f"Manufacturing Date: {self.manufacturing_date}")
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")


car = Car("2026-06-28", "Black", "BMW")

car.display()
