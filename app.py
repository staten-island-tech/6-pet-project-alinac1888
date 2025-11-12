class pet:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper"])