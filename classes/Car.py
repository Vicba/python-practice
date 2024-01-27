
class Car:
    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        return f"Car: {self.name}, {self.color}, {self.year}"
    
    def drive(self):
        print(f"{self.name} VROOM VROOM!")


class ElectricCar(Car):
    def __init__(self, name, color, year, price, battery_size):
        super().__init__(name, color, year, price)
        self.battery_size = battery_size

    def __str__(self):
        return f"Electric Car: {self.name}, {self.color}, {self.year}, {self.battery_size}"

    def drive(self):
        print(f"{self.name} ZOOM ZOOM!")


if __name__ == "__main__":
    car = Car("Tesla", "Red", 2020, 10000)
    print(car)
    car.drive()
