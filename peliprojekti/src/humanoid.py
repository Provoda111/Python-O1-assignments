class Humanoid:
    def __init__(self, name):
        self.healthPoint = 100
        self.armour = 0
        self.name = name

    def ChangeHP(self, amount):
        #TODO If attacked by melee takes armour first

        # Checks if amount to change is bigger than 100 or lower than 1
        if amount + self.healthPoint > 100 or amount - self.healthPoint < 1:
            print("HP can't be bigger than 100 or lower than 0")
        else:
            # Sets updated HP
            self.healthPoint = self.healthPoint
            print(f"{self.name} HP has been changed to: {self.healthPoint}")

    def ChangeArmour(self, amount):
        # Checks if amount to change is bigger than 100 or lower than 1
        if amount < 1 or amount > 100:
            print("Armour can't be bigger than 100 or lower than 0")
        else:
            # Sets updated Armour
            self.armour = amount
            print(f"{self.name} HP has been changed to: {self.armour}")