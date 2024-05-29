
class Buyer:
    def __init__(self, name, money, Inventory):
        self.name = name
        self.money = money
        self.Inventory = Inventory

    def __str__(self):
        return f"Buyer: {self.name}, {self.money}, {self.Inventory}"
    
    def buy(self, item):
        self.Inventory.addItem(item)
        self.money -= item.price

    def sell(self, item):
        self.Inventory.removeItem(item)
        self.money += item.price

    def getMoney(self):
        return "Money: " + str(self.money) + " dollars"

    def printInventory(self):
        print(self.Inventory)

    def drive_car(self, item):
        item.drive()


if __name__ == "__main__":
    pass

    

