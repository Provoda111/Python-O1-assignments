class Inventory:
        def __init__(self, owner):
            self.items = list()
            self.owner = owner
            
        def ListInventoryItems(self):
            print("-----INVENTORY-----")
            if self.items:
                for item in self.items:
                    print(f"| Item No {self.items.index(item) + 1} - {item.name} |\n| Price: {item.price} coins |\n| Description: {item.description} |\n")
            else:
                print(f"You don't have anything")
                
        def AddItem(self, item):
            try:
                self.items.append(item)
                print(f"Added an item {item.name} to player's inventory")
                print(f"To check {item.name}'s characteristics you should check your inventory")
                #if item.type == "shield":
                #    self.owner.armour                
            except:
                print(f"UNKNOWN ERROR. Couldn't add an {item.name} to player's inventory")
            
        def RemoveItem(self, item):
            try:
                self.items.remove(item)
                print(f"Succesfully removed an item '{item.name}' from your inventory")
            except:
                print(f"Couldn't remove an item '{item.name}' from your inventory")
            
        def ClearInventory(self):
            self.items.clear()

        def ItemIsInInventory(self, itemName):
            for item in self.items:
                if itemName == item.name:
                    return True

        def GetItemByName(self, itemName):
            for item in self.items:
                if itemName == item.name:
                    return item