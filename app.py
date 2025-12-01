class pet:
    def __init__(self, name, money, inventory, happy, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happy
        self.hunger = hunger
        happy = 50
        hunger = 50
        self.living = True

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def maybe_boredom(self):
        while self.living == True:
            if self.happiness >= 50 and self.happiness <= 100:
                print(f"{self.name} is content, happiness is at {self.happiness}")
            if self.happiness < 50 and self.happiness >= 0:
                print(f"{self.name} is filler, happiness is at {self.happiness}")
                self.happiness -= 1
            if self.happiness > 100:
                self.happiness = 100
                print(f"{self.name} filler, happiness is at {self.happiness}")
            else:
                print(f"sad {self.name}")
                self.living = False

    def starve(self):
        while self.living == True:
            if self.hunger >= 50 and self.hunger <= 100:
                print(f"{self.name} is not hungry, hunger is at {self.hunger}")
            if self.hunger < 50 and self.hunger >= 0:
                print(f"{self.name} is hungry, hunger is at {self.hunger}")
                happiness -= 1
            if self.hunger > 100 and self.hunger:
                hunger = 100
                print(f"{self.name} is overfed, hunger is at {self.hunger}")
            else:
                print(f"neglected {self.name}")
                self.living = False

    def feed(self):
        while 

usagi = pet("usagi", 2000000000000000, ["cheeseburger, hamburger, big mac, whopper, pibbl"])
print(usagi.__dict__)

usagi.feed("hamburger")

