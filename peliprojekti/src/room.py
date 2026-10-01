class Room:
    def __init__(self, name, description, icon, locked):
        self.name = name
        self.description = description
        self.items = []
        self.icon = icon
        self.locked = locked

    # Opens the room
    def OpenRoom(self):
        self.locked = False

    # Closes the room
    def CloseRoom(self):
        self.locked = True

    