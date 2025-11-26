class pet:
    def __init__(self, name, money, inventory, happy, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.__happiness = happy
        self.hunger = hunger
        happy = 100
        hunger = 100

    food = ["cheeseburger", "hamburger", "big mac", "whopper", "pibbl"]

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def starve(self, item, hunger):
        item = 1
        hunger -= item
        if hunger < 50:
            print(f"{self.name} is hungry")
            happiness -= item

    def feed(self, food, hunger):
        food = 20
        self.hunger += food
        if self.hunger >= 50 and hunger <= 100:
            print(f"{self.name} is not hungry")
        if self.hunger < 50 and hunger >= 0:
            print(f"{self.name} is hungry")
        if self.hunger > 100:
            print(f"{self.name} is overfed")
        print(self.hunger)

    

usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper, pibbl"], 100, 100)
print(usagi.__dict__)

usagi.feed("hamburger")

