class ItemShop:
    def __init__(self):
        self.availableItems = list()
        

    # Returns a player a list of the available items
    def ListAvailableItems(self):
        for item in self.availableItems:
            print(f"| {self.availableItems.index(item) + 1} - {item.name} |\n| Price: {item.price} coins |\n| Description: {item.description} |\n")

    # Adds a specified item into item shop's available items
    def AddItemToShop(self, itemToAdd):
        self.availableItems.append(itemToAdd)
        print(f"Succesfully added {itemToAdd.name} to shop")

    # Removes a specified (target) item. 
    def RemoveItem(self, targetItem):
        self.availableItems.remove(targetItem)
        print(f"Succesfully removed {targetItem} from shop")

    def GetItemIndex(self, itemName):
        for item in self.availableItems:
            if item.name == itemName:
                return self.availableItems.index(item)
        
    def ItemIsInShop(self, itemName):
        for item in self.availableItems:
            if item.name == itemName:
                return True