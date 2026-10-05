class Room:
    def __init__(self, name, description, icon, locked):
        self.name = name
        self.description = description
        self.items = []

        # The icon is a char and it should be a first letter or a few letters from room's name
        self.icon = icon

        # Is the room locked or not
        self.locked = locked

        # List for all of those who are inside of a room
        self.guests = []

    # Opens the room
    def OpenRoom(self):
        self.locked = False

    # Closes the room
    def CloseRoom(self):
        self.locked = True

    def AddGuest(self, guest):
        self.guests.append(guest)

    def RemoveGuest(self, guest):
        self.guests.remove(guest)

    # This method is responsible for creating a random events in room that player enters.
    # This method is called ONLY WHEN PLAYER CHANGES ROOM not in start
    # Events can be attacked by ghost, player found armour or HP potion
    def RandomEvent(self, player, gameManager):
        import random
        randomEvent = random.randint(1, 4)
        match randomEvent:
            case 1:
                print("Ghost attacked you!!")
                player.ChangeHP(player.healthPoint - random.randint(5, 12))
            case 2:
                print("You found armour")
                player.ChangeArmour(player.armour + random.randint(10, 20))
            case 3:
                print("You found HP potion")
                player.ChangeHP(player.healthPoint + random.randint(10, 15))
            case 4:
                print("You found nothing")
            case 5:
                print("You found key. Maybe it open's something")
                player.inventory.AddItem(gameManager.GetItemByName("Key"))