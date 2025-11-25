class pet:
    def __init__(self, name, money, inventory, happy, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.__happiness = happy
        self.hunger = hunger

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    

    def starve(self, item):
        item = 1
        hunger -= item
        if hunger < 50:
            print(f"{self.name} is hungry")
            happiness -= item

    def feed(self, food):
        food = 20
        hunger += food
        if hunger >= 50 and hunger <= 100:
            print(f"{self.name} is not hungry")
        if hunger < 50 and hunger >= 0:
            print(f"{self.name} is hungry")


usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper, pibbl"], 1000, 100)
print(usagi.__dict__)

usagi.buy({"title": "rod", "atk": 6000})
usagi.feed(food: "")

