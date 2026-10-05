from inventory import Inventory

class Player:
    player = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = Inventory(self)
        self.actualRoom = None

    def ChangeRoom(self, room):
        self.actualRoom = room
        print(f"You have entered a room {self.actualRoom.name} | Description: {self.actualRoom.description}")

    def SaveProgress(self):
        pass