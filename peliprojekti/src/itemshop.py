class ItemShop:
    availableItems = ("Dagger", "Sword", "Shield", "Iron Armor", "Diamond Sword")

    def ListAvailableItems(self):
        for item in self.availableItems:
            print(f"Item {item} {item.index(item)}")