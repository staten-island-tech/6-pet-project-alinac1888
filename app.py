class pet:
    def __init__(self, name, money, inventory, happy, hunger):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happy
        self.hunger = hunger
        hunger = 50
        self.living = True

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def maybe_boredom(self):
        while self.living == True:
            if self.happiness >= 50 and self.happiness <= 100:
                print(f"{self.name} is content, happiness is at {self.happiness}")
            elif self.happiness < 50 and self.happiness >= 0:
                print(f"{self.name} is filler, happiness is at {self.happiness}")
                happy -= 1  
            elif self.happiness > 100:
                self.happiness = 100
                print(f"{self.name} filler, happiness is at {self.happiness}") 
            else:
                print(f"sad {self.name}")
                self.living = False

    def starve(self):
        while self.living == True:
            if self.hunger >= 50 and self.hunger <= 100:
                print(f"{self.name} is not hungry, hunger is at {self.hunger}")
            elif self.hunger < 50 and self.hunger >= 0:
                print(f"{self.name} is hungry, hunger is at {self.hunger}")
                happiness -= 1
            elif self.hunger > 100 and self.hunger <= 130:
                hunger = 100
                print(f"{self.name} is overfed, hunger is at {self.hunger}")
            elif self.hunger > 130:
                print(f"{self.name} DEAD")
                self.living = False
            else:
                print(f"neglected {self.name}")
                self.living = False

    def feed(self, eat):
        while self.living == True:
            eat = input(f"Feed {self.name}")
            if eat in self.inventory:
                hunger += 10
            if eat not in self.inventory:
                print(f"food not found in {self.name}'s inventory")
        if self.living == False:
            print(f"{self.name} is dead")
    
    def stats(self):
        print(self.__dict__)
        print(f"hunger bar:{self.starve}")

usagi = pet("usagi", 2000000000000000, ["cheeseburger", "hamburger", "big mac", "whopper", "pibbl", "lemons"], 50, 50)

usagi.stats()
usagi.feed("lemons")

