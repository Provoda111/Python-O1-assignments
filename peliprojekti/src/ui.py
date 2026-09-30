import time
import os

class UI:
    def DrawMainMenu(self, player, gameManager):
        print("-----MAIN MENU-----")
        print("1 - Add item to inventory")
        print("2 - Check your inventory")
        print("3 - Delete item from your inventory")
        #print("4 - Enter the castle")
        print("4 - Leave the game")
        playerChoice = input("What will you choose? \n")
        match playerChoice:
            case 1 | "1":
                print("You chose 1 - Add item to your inventory\n")
                self.AddItemUI(gameManager, player)
            case 2 | "2":
                print("You chose 2 - Check your inventory\n")
                self.InventoryUI(player, gameManager)
            case 3 | "3":
                print("You chose 3 - Delete item from your inventory\n")
                if len(player.inventory.items) < 1:
                    print("You don't have anything")
                else:
                    pass
            case 4 | "4":
                print("You chose 4 - Leave the game\n")
                os.abort()
            case "Admin" | "admin":
                print("You've entered admin mode")
                self.DrawAdminMenu()

    # Draws a player available items in item shop
    def AddItemUI(self, gameManager, player): 
        print("-----ITEM SHOP-----\n")

        # Checks if there is any allowed items in shop
        if len(gameManager.itemShop.availableItems) >= 1:

            #Prints every allowed item (index (index + 1) - (item name)) 
            gameManager.itemShop.ListAvailableItems()
            time.sleep(2)
            selectedItem = input("\nMitä valitset?\n")

            # Prevents player getting asked item twice for balance😂
            if player.inventory.ItemIsInInventory(selectedItem):
                print(f"You already have {selectedItem}")

            # If player doesn't have asked item, it will be added
            else:

                # Checks if the asked item by player is in allowed items
                if gameManager.itemShop.ItemIsInShop(selectedItem):
                    itemsIndex = gameManager.itemShop.GetItemIndex(selectedItem)
                    player.inventory.AddItem(gameManager.itemShop.availableItems[itemsIndex])

                # If there is no asked item in allowed items, then it will not add
                else:
                    print(f"{selectedItem} isn't added because it isn't in available items")
        else:
            print("At current time there is no available items")
        print("Bringing you back to main menu in few seconds.....")
        time.sleep(1.5)
        self.DrawMainMenu(player, gameManager)

    def InventoryUI(self, player, gameManager):
        player.inventory.ListInventoryItems()
        time.sleep(1.8)
        self.DrawMainMenu(player, gameManager)


    def DrawCastle(self, player, gameManager, room):
        # for x in 
        pass


    #TODO Make admin menu if i want
    def DrawAdminMenu(self):
        print("-----ADMIN MENU-----")
        print("1 - Check target player's inventory:")
        print("Leave admin menu")