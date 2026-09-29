import time

class UI:
    def DrawMainMenu(self):
        print("Valitse mitä haluat tehdä:")
        print("1 - Add item to inventory")
        print("2 - Check your inventory")
        print("3 - Delete item from your inventory")
        print("4 - Leave the game")
        playerInput = input("\n")
        match playerInput:
            case 1 | "1":
                print("You chose 1 - Add item to your inventory\n")
                self.AddItemUI()
            case 2 | "2":
                print("You chose 2 - Check your inventory\n")
            case 3 | "3":
                print("You chose 3 - Delete item from your inventory\n")
            case 4 | "4":
                print("You chose 4 - Leave the game\n")
            case "Admin" | "admin":
                print("You've entered admin mode")

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
        print("You are checking your inventory\nI'll list all of your items\n")
        if inventory.inventoryItems.count() >= 1:
            print()
            for i in inventory.allowedItems:
                print(f"{i.index + 1} - {i}")
        else:
            print("Sinulla ei ole tavaroita")
            print("Palautan sinut takaisin muutaman sekunnin kuluttua")
            time.sleep(1.8)
            #ui.DrawMainMenu()
    
    def DrawAdminMenu(self):
        pass