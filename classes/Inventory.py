
class Inventory:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def __str__(self):
        return ', '.join(str(item) for item in self.items)
    

if __name__ == "__main__":
    inventory = Inventory()
    print(inventory)