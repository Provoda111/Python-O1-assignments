from inventory import Inventory

class Player:
    player = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = Inventory(self)

    def Attack(self, weapon):
        pass