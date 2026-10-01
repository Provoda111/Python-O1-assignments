class Inventory:
        def __init__(self, owner):
            self.items = tuple()
            

        def ListInventoryItems(self):
            print("-----INVENTORY-----")
            if self.items:
                for item in self.items:
                    print(f"| Item No {self.items.index(item) + 1} - {item.name} |\n| Price: {item.price} coins |\n| Description: {item.description} |\n")
            else:
                print(f"You don't have anything")
                
        def AddItem(self, item):
            #TODO make method in gamemanager.py??? for this tuple-list manipulation
            tmpList = list(self.items)
            tmpList.append(item)
            self.items = tuple(tmpList)
            print(f"Added an item {item.name} to player's inventory")
            print(f"To check {item.name}'s characteristics you should check your inventory")

        def RemoveItem(self, item):
            try: 
                tmpList = list(self.items)
                tmpList.remove(item)
                self.items = tuple(tmpList)
                print(f"Succesfully removed an item '{item.name}' from your inventory")
            except:
                print(f"Couldn't remove an item '{item.name}' from your inventory")
            

        def ClearInventory(self):
            self.items = tuple()

        def ItemIsInInventory(self, itemName):
            for item in self.items:
                if itemName == item.name:
                    return True