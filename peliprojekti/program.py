# Tämä on Gleb Balajevin tekemä peli
# Varoitus! Jos henkilö on alle
class UI:
    def DrawMainMenu(self):
        print("Hello")

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def LogIn(self):
        print("Hei! Ennen kuin aloitat pelaamisen, haluaisin tallentaa tietyn tiedon sinusta")
        if (playerAge < 12):
            print ("Hei! Si")
        print(f"Hienoa! Sinun nimesi on {playerName} ja ikäni on {playerAge}")

class Inventory:
    inventoryItems = []
    def AddItem(itemName):
        f"Added an item {itemName} to player's inventory"

ui = UI()
inventory = Inventory()

playerName = str(input("Kirjoita oma nimesi:\n"))
playerAge = int(input("Kirjoita oma ikä:\n"))
player = Player(playerName, playerAge)


