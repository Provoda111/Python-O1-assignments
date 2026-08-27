# Tämä on Gleb Balajevin tekemä peli
# Varoitus! Jos henkilö on alle

import os
import time

class Inventory:
    inventoryItems = []
    allowedItems = ["Dagger", "Sword", "Shield", "Iron Armor", "Diamond Sword"]
    def AddItem(itemName):
        f"Added an item {itemName} to player's inventory"
    def ListAllowedItems():
        print()
    def ListInventoryItems():
        print()

class UI:
    def DrawMainMenu(self):
        print("Valitse mitä haluat tehdä:")
        print("1 - Lisätä tavaroita tavaraluetteloon")
        print("2 - Tarkista tavaraluettelo")
        print("3 - Poista tavaroita tavaraluettelosta")
        print("4 - Poistua pelistä")
        playerInput = input("\n")
        match playerInput:
            case 1 | "1":
                print("Valitsit 1 - Lisätä tavaroita tavaraluetteloon\n")
                self.AddItemUI()
            case 2 | "2":
                print("Valitsit 2 - Tarkista tavaraluettelo\n")
            case 3 | "3":
                print("Valitsit 3 - Poista tavaroita tavaraluettelosta\n")
            case 4 | "4":
                print("Valitsit 4 - Poistua pelistä\n")
    def AddItemUI(self):
        inventory = Inventory()
        print("Olet tavaroiden hanke sivussa.\nListan sallittuja tavaroita sinulle")
        if len(inventory.allowedItems) >= 1:
            for i in range(len(inventory.allowedItems)):
                print(f" {i+1} - {inventory.allowedItems[i]}")
            time.sleep(2)
            playerInput = input("\nMitä valitset?\n").strip().lower()
            match playerInput:
                case [*inventory] if str(playerInput) in inventory.allowedItems:
                    print("Hei!")

    def InventoryUI():
        inventory = Inventory()
        print("Olet tavaraluettelossa.\nKirjoitan alas sinun hallussa olevat tavarat\n")
        if inventory.inventoryItems.count() >= 1:
            print()
        for i in range(len(inventory.inventoryItems)):
            print()

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.LogIn()
    def LogIn(self):
        print("Aloitan minimi vaatimuksien tarkistamisen")
        if (self.age < 12):
            print("Hei! Sinä olet liian alaikäinen tälle pelille")
            os.abort()
        else:
            print(f"Hienoa! Kirjauduit sisään. Sinun nimesi on {playerName} ja ikäsi on {playerAge}.\n")
        time.sleep(2)

ui = UI()
# inventory = Inventory()

print("Hei! Tervetuloa peliin. Aloitetaan tietojen keräämisestä.")

playerName = str(input("Kirjoita oma nimesi:\n"))
playerAge = int(input("Kirjoita oma ikä:\n"))
player = Player(playerName, playerAge)
ui.DrawMainMenu()


