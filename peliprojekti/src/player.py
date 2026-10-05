from inventory import Inventory
from humanoid import Humanoid

class Player(Humanoid):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.inventory = Inventory(self)
        self.actualRoom = None
        self.info = dict()

    def ChangeRoom(self, room):
        self.actualRoom = room
        room.AddGuest(self)
        print(f"You have entered a room {self.actualRoom.name} | Description: {self.actualRoom.description}")

    def SaveProgress(self):
        import os
        directory_name = "savefiles"
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{directory_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        with open("savefiles/savefile.txt", "a") as file:
            file.write("Now i am the king")
        #TODO JSON saving
        pass