class ItemShop:
    itemsToAdd = ("Dagger", "Sword", "Shield", "Iron Armor", "Diamond Sword")

    def __init__(self):
        self.availableItems = tuple()

    # Returns a player a list of the available items
    def ListAvailableItems(self):
        for item in self.availableItems:
            print(f"Item No {self.availableItems.index(item) + 1} - {item}")


    # Adds a specified item into item shop's available items
    def AddItem(self, itemToAdd):
        tempList = list(self.availableItems)
        tempList.append(self.itemsToAdd)
        self.availableItems = tuple(self.availableItems)

    # Removes a specified (in this context - target) item. 
    def RemoveItem(self, targetItem):
        tempList = list(self.availableItems)
        tempList.remove(targetItem)
        self.availableItems = tuple(self.availableItems)