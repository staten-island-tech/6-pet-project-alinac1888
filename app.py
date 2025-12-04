class pet:
    def __init__(self, name, money, inventory, happy, hunger, living):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happy
        self.hunger = hunger
        hunger = 50
        happy = 50
        self.living = living
        living = True

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

    def maybe_boredom(self):
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
        if self.hunger >= 50 and self.hunger <= 100:
            print(f"{self.name} is not hungry, hunger is at {self.hunger}")
        elif self.hunger < 50 and self.hunger >= 0:
                print(f"{self.name} is hungry, hunger is at {self.hunger}")
                happiness -= 1
        elif self.hunger > 100 and self.hunger <= 130:
                print(f"{self.name} is overfed, hunger is at {self.hunger}")
        elif self.hunger > 130:
            print(f"{self.name} DEAD")
            self.living = False
        else:
            print(f"neglected {self.name}")
            self.living = False

    def feed(self, eat):
        if eat in self.inventory:
            self.hunger += 10
            print(f"{self.name} is now at {self.hunger}/100 hunger")
        else:
            print(f"food not found in {self.name}'s inventory")
    
    def stats(self):
        print(self.__dict__)

    def gameshhssjsa(self, choice):
      while self.living == True:
        for i in pet:
            if choice == i:
                print("test")
    gameshhssjsa()


usagi = pet("usagi", 2000000000000000, ["cheeseburger", "hamburger", "big mac", "whopper", "pibbl"], 50, 50, True)

usagi.stats()
usagi.gameshhssjsa()


    
    