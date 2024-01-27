from Car import Car, ElectricCar
from Inventory import Inventory
from Buyer import Buyer



def main():
    car1 = Car("Volvo", "Red", 2020, 100000)
    car2 = Car("Toyota", "Blue", 2019, 20000)
    electricCar1 = ElectricCar("Tesla", "Red", 2020, 100000, 100)

    buyer1 = Buyer("John", 100000, Inventory())
    buyer1.buy(car1)

    buyer2 = Buyer("Jane", 200000, Inventory())
    buyer2.buy(car2)
    buyer2.buy(electricCar1)

    print("buyer1")
    buyer1.printInventory()
    print(buyer1.getMoney())

    print("----")
    print("buyer2")
    buyer2.printInventory()
    print(buyer2.getMoney())
    print("after selling the toyota")
    buyer2.sell(car2)
    buyer2.printInventory()
    print(buyer2.getMoney())

    print("lets drive the cars")
    buyer2.drive_car(electricCar1)
    buyer1.drive_car(car1)



if __name__ == "__main__":
    main()