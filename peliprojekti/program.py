# Tämä on Gleb Balajevin tekemä peli

import os
import time

class GameManager:
    ## TODO THINK ABOUT PLAYERS LIST/SET
    players = list()

    def LogIn(self):
        print("Aloitetaan käyttäjän luomisesta")
        while True:
            playerAgeInput = int(input("Kirjoita sinun ikäsi: "))
            playerNameInput = input("Kirjoita sinun nimesi: ")
            if playerAgeInput > 12 and playerNameInput != None and playerNameInput != "":
                print("Account created succesfully")
                break
            else:
                print("Can't create an account for you")
    def AddPlayer(self, playerNameInput, playerAgeInput):
        newPlayer = Player(playerNameInput, playerAgeInput)
        newPlayer.player = {
            "Name" : playerNameInput,
            "Age"  : playerAgeInput,
            }
        pass
    def DeletePlayer(self, player):
        pass
    
    
# This class is responsible for drawing UI for the user
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

    def AddItemUI(self, itemShop, playerInventory): 
        print("Olet tavaroiden hanke sivussa.\nListan sallittuja tavaroita sinulle")

        # Checks if there is any allowed items in shop
        if len(itemShop.allowedItems) >= 1:

            #Prints every allowed item (index (index + 1) - (item name)) 
            for i in range(len(itemShop.allowedItems)):
                print(f" {i+1} - {itemShop.allowedItems[i]}")
            time.sleep(2)
            playerInput = input("\nMitä valitset?\n")

            # Prevents player getting asked item twice
            # No logic, just balance 😂
            if playerInput in playerInventory.inventoryItems:
                print(f"You already have {playerInput}")

            # If player doesn't have asked item, it will be added
            else:
                # Checks if the asked item by player is in allowed items
                if playerInput in itemShop.allowedItems:
                    print("Item is added")
                    playerInventory.inventoryItems.append(playerInput)

                # If there is no asked item in allowed items, then it will not add
                else:
                    print("Item isn't added")
        else:
            print("At current time there is no available items")
            print("Bringing you back to main menu in few seconds.....")
            time.sleep(1.5)
            self.DrawMainMenu()

    def InventoryUI(inventory):
        print("Olet tavaraluettelossa.\nKirjoitan sinun hallussa olevat tavarat\n")
        if inventory.inventoryItems.count() >= 1:
            print()
            for i in inventory.allowedItems:
                print(f"{i.index + 1} - {i}")
        else:
            print("Sinulla ei ole tavaroita")
            print("Palautan sinut takaisin muutaman sekunnin kuluttua")
            time.sleep(1.8)
            #ui.DrawMainMenu()

class Player:
    player = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.LogIn()
    class Inventory:
        inventoryItems = list()

        inventory = dict()

        

        def AddItem(itemName):
            print(f"Added an item {itemName} to player's inventory")
        def ListInventoryItems():
            print()
        def RemoveItem(itemName):
            print()
        def ClearInventory():
            print()

class ItemShop:
    availableItems = ("Dagger", "Sword", "Shield", "Iron Armor", "Diamond Sword")

    def ListAvailableItems(self):
        for item in self.availableItems:
            print(f"Item {item} {item.index(item)}")
        pass
    pass

class Castle:
    pass

class CastleRoom(Castle):
    pass

gameManager = GameManager()


itemShop = ItemShop()
itemShop.ListAvailableItems()
print("Hei! Tervetuloa peliin.")
gameManager.LogIn()