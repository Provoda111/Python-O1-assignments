import time
import os

class UI:
    def DrawMainMenu(self, player, gameManager):
        print("-----MAIN MENU-----")
        print("1 - Enter the item shop")
        print("2 - Check your inventory")
        print("3 - Enter the castle")
        print("4 - Leave the game\n")
        while True:
            playerChoice = input("What will you select:\n")
            match playerChoice:
                case 1 | "1":
                    self.AddItemUI(gameManager, player)
                case 2 | "2":
                    self.InventoryUI(player, gameManager)
                case 3 | "3":
                    self.DrawCastle(player, gameManager)
                case 4 | "4":
                    #TODO Save game progress to the JSON file
                    os.abort()
                case _:
                    print("Invalid input. Try again")
                
    # Draws a player available items in item shop
    def AddItemUI(self, gameManager, player): 
        print("-----ITEM SHOP-----\n")

        # Checks if there is any allowed items in shop
        if gameManager.itemShop.availableItems:

            #Prints every allowed item (index (index + 1) - (item name)) 
            gameManager.itemShop.ListAvailableItems()
            time.sleep(2)
            selectedItem = input("\nMitä valitset?\n")

            # Prevents player getting asked item twice for balance😂
            if player.inventory.ItemIsInInventory(selectedItem):
                print(f"You already have {selectedItem}\n")

            # If player doesn't have asked item, it will be added
            else:

                # Checks if the asked item by player is in allowed items
                if gameManager.itemShop.ItemIsInShop(selectedItem):
                    itemsIndex = gameManager.itemShop.GetItemIndex(selectedItem)
                    player.inventory.AddItem(gameManager.itemShop.availableItems[itemsIndex])

                # If there is no asked item in allowed items, then it will not add
                else:
                    print(f"{selectedItem} isn't added because it isn't in available items\n")
        # If there is no items
        else:
            print("At current time there is no available items\n")
        print("Bringing you back to main menu in few seconds.....")
        time.sleep(1.5)
        self.DrawMainMenu(player, gameManager)

    def InventoryUI(self, player, gameManager):
        player.inventory.ListInventoryItems()
        if player.inventory.items:
            try:
                print("Do you wish to delete item? (Yes/No)")
                playerChoice = input("\n")
                match playerChoice:
                    case "Yes":
                        print("Write an item name to delete it")
                        selectedItem = input("\n")
                        if player.inventory.ItemIsInInventory(selectedItem):
                            player.inventory.RemoveItem(player.inventory.GetItemByName(selectedItem))
                    case _:
                        print("Unknown response")
            except Exception as error:
                print(f"Error happened: {error}")
        print("Returning to the main menu.....")
        time.sleep(1.8)
        self.DrawMainMenu(player, gameManager)

    # Draws a castle room for the player for example to choose if he wants to go forward, or back and etc.
    def DrawCastle(self, player, gameManager):
        self.DrawRooms(player, gameManager)
        print("-----MENU-----")
        print("1 - Go forward")
        print("2 - Go back")
        print("3 - Back to the main menu")
        while True:
            try:
                playerChoice = input("What will you select? ")
                match playerChoice:
                    case "1" | 1:
                        if gameManager.rooms.index(player.actualRoom) < len(gameManager.rooms):
                            player.ChangeRoom(gameManager.rooms[gameManager.rooms.index(player.actualRoom) + 1])
                        else:
                            print("Can't go any forward")
                    case "2" | 2:
                        if gameManager.rooms.index(player.actualRoom) > 0:
                            player.ChangeRoom(gameManager.rooms[gameManager.rooms.index(player.actualRoom) - 1])
                        else:
                            print("Can't go any backwards")
                    case "3" | 3:
                        print("Going back to the main menu....")
                    case _:
                        print("Wrong input. Try again")
            except Exception as error:
                print(f"Error happened. Error: {error}. Try again")

    def DrawRooms(self, player, gameManager):
        rooms_list = []
        for room in gameManager.rooms:
            rooms_list.append(room.icon)
            
        roomsToPrint = " ".join(rooms_list)
        print(roomsToPrint)
        
        current_index = gameManager.rooms.index(player.actualRoom)
        offset = 0
        for i in range(current_index):
            offset += len(gameManager.rooms[i].icon) + 1
                
        room_icon_len = len(player.actualRoom.icon)
        pointer_offset = offset + (room_icon_len // 2)
            
        print(" " * pointer_offset + "↑")
        print(" " * pointer_offset + "Player")