class Item:
    def __init__(self, name, type, price = 0, description = "Item doesn't have a description"):
        self.name = name
        self.price = price
        self.description = description
        self.type = type

    # Returns a name, price and a description of the item
    def Info(self):
        return f"{self.name} has a price tag {self.price} and description {self.description}"