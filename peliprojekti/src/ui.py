import time
import os

class UI:
    def DrawMainMenu(self, player, gameManager):
        print("-----MAIN MENU-----")
        print("1 - Add item to inventory")
        print("2 - Check your inventory")
        print("3 - Delete item from your inventory")
        print("4 - Leave the game")
        playerChoice = input("What will you choose? \n")
        match playerChoice:
            case 1 | "1":
                print("You chose 1 - Add item to your inventory\n")
                self.AddItemUI(gameManager.itemShop, player)
            case 2 | "2":
                print("You chose 2 - Check your inventory\n")
                self.InventoryUI()
            case 3 | "3":
                print("You chose 3 - Delete item from your inventory\n")
            case 4 | "4":
                print("You chose 4 - Leave the game\n")
                os.abort()
            case "Admin" | "admin":
                print("You've entered admin mode")
                self.DrawAdminMenu()

    # Draws a player available items in item shop
    def AddItemUI(self, itemShop, player): 
        print("-----ITEM SHOP-----")

        # Checks if there is any allowed items in shop
        if len(itemShop.availableItems) >= 1:

            #Prints every allowed item (index (index + 1) - (item name)) 
            for i in range(len(itemShop.availableItems)):
                #TODO draw item description
                print(f" {i+1} - {itemShop.availableItems[i]}")
            time.sleep(2)
            itemInput = input("\nMitä valitset?\n")

            # Prevents player getting asked item twice for balance😂
            if itemInput in player.inventory.items:
                print(f"You already have {itemInput}")

            # If player doesn't have asked item, it will be added
            else:
                # Checks if the asked item by player is in allowed items
                if itemInput in itemShop.availableItems:
                    print(f"{itemInput} is added")
                    player.inventory.items.append(itemInput)

                # If there is no asked item in allowed items, then it will not add
                else:
                    print(f"{itemInput} isn't added because it isn't in ")
        else:
            print("At current time there is no available items")
            print("Bringing you back to main menu in few seconds.....")
            time.sleep(1.5)
            self.DrawMainMenu()

    def InventoryUI(self, player):
        print("You are checking your inventory\nI'll list all of your items\n")
        if player.inventory.count() >= 1:
            pass
        else:
            print("Unfortunately you don't have any items")
            time.sleep(1.8)
            self.DrawMainMenu()
    
    def DrawAdminMenu(self):
        print("-----ADMIN MENU-----")
        print("1 - Check target player's inventory:")
        print("Leave admin menu")
        pass