class pet:
    def __init__(self, name, money, inventory, happy):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.__happiness = happy
        # self.hunger = hunger
        # hunger = 100
        happy = 100

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    
    # def feed(self, food):
    #     food = 20
    #     self.hunger += food
    #     print(f"{self.name}'s hunger is at {}")

    def play(self, item):
        item = 10
        happy += item

        

usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper, pibbl"], 1000)
print(usagi.__dict__)

usagi.buy({"title": "rod", "atk": 6000})
usagi.play({""})

