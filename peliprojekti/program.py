# Tämä on Gleb Balajevin tekemä peli
# Varoitus! Jos henkilö on alle

import os
import time

# This class is responsible for player's inventory interaction
# 
class Inventory:
    inventoryItems = []
    allowedItems = ["Dagger", "Sword", "Shield", "Iron Armor", "Diamond Sword"]
    def AddItem(itemName):
        print(f"Added an item {itemName} to player's inventory")
    def ListAllowedItems():
        print()
    def ListInventoryItems():
        print()
    def RemoveItem(itemName):
        print()
    def ClearInventory():
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
            playerInput = input("\nMitä valitset?\n").strip()
            if playerInput in inventory.inventoryItems:
                print(f"You already have {playerInput}")
            
            else:
                if playerInput in inventory.allowedItems:
                    print("Item is added")
                    inventory.inventoryItems.append(playerInput)
                else:
                    print("Item isn't added")
        else:
            print("At current time there is no available items")
            print("Bringing you back to main menu")
            self.DrawMainMenu()

    def InventoryUI():
        inventory = Inventory()
        print("Olet tavaraluettelossa.\nKirjoitan sinun hallussa olevat tavarat\n")
        if inventory.inventoryItems.count() >= 1:
            print()
            for i in inventory.allowedItems:
                print(i)
        else:
            print("Sinulla ei ole tavaroita")
            print("Palautan sinut takaisin muutaman sekunnin kuluttua")
            time.sleep(1.5)
            ui.DrawMainMenu()

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
        time.sleep(1.5)

ui = UI()
# inventory = Inventory()

print("Hei! Tervetuloa peliin. Aloitetaan tietojen keräämisestä.")

ui.cont()

playerName = str(input("Kirjoita oma nimesi:\n"))
playerAge = int(input("Kirjoita oma ikä:\n"))
player = Player(playerName, playerAge)
ui.DrawMainMenu()


