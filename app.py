class pet:
    def __init__(self, name, money, inventory, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.hunger = hunger

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    
    def starvation(self, item):
        self.hunger()

usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper, pibbl"], 100)
print(usagi.__dict__)

usagi.buy({"title": "rod", "atk": 6000})


