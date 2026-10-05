from player import Player
from ui import UI
from itemshop import ItemShop
from item import Item
from room import Room

# GameManager class main responsibility is to organize a interaction between other classes, calling various functions, methods
# and taking variables. GameManager is a class where game initializes, creates necessary variables, files and etc.
class GameManager:
    
    def __init__(self):
        self.players = []
        self.ui_control = UI()
        self.itemShop = ItemShop()
        self.startRoom = None
        self.rooms = list()
        self.itemsInGame = []

    def CreateFirstItems(self):
            # Adding to game melee weapon's
            self.itemShop.AddItemToShop(Item("Dagger", "Attack", 25, "Cool melee weapon"))
            self.AddItemToGame(Item("Dagger", "Attack", 25, "Cool melee weapon"))
            self.itemShop.AddItemToShop(Item("Sword", "Attack",45, "Cool and strong melee weapon"))
            self.AddItemToGame(Item("Sword", "Attack",45, "Cool and strong melee weapon"))

            # Adding to game a key 
            #TODO FUNCTIONALITY FOR KEY
            self.AddItemToGame(Item("Key", "Misc.", 0, "Secret key"))


    def AddItemToGame(self, item):
        self.itemsInGame.append(item)
        
    def CreateRooms(self):
        self.rooms += [Room("Lobby", "First room in castle", "L", False), Room("Visitor's bedroom", "Visitors can sleep here", "VB1", False), Room("Main bedroom", "There is a story, that here is sleeping prince of the castle", "MB1", False), Room("Armory", "Here is all weapons of this castle", "A", False), Room("Throne", "King is here", "Thr", True)]

    # Creates a player character to the game
    def LogIn(self):
        succesfullRegistration = False
        print("Let's start with creating your character")
        while succesfullRegistration != True:
            try:
                playerAgeInput = int(input("Kirjoita sinun ikäsi: "))
                playerNameInput = input("Kirjoita sinun nimesi: ")

                # If player is older than 12 and player name input is correct then it creates an account
                if playerAgeInput > 12 and playerNameInput != None and playerNameInput != "":
                    print("Account created succesfully")
                    succesfullRegistration = True
                else:
                    print("Can't create an account for you")

            except ValueError:
                print("Error in name or age input, try again")
        self.AddPlayer(playerNameInput, playerAgeInput)

        # Adds a new player to the game and lists
    def AddPlayer(self, playerNameInput, playerAgeInput):
        newPlayer = Player(playerNameInput, playerAgeInput)
        newPlayer.info = {
            "Name" : playerNameInput,
            "Age"  : playerAgeInput }
        self.players.append(newPlayer)

        self.InitGame(newPlayer)

    def DeletePlayer(self, targetPlayer):
        if targetPlayer in self.players:
            print(f"Deleting a player {targetPlayer["Name"]}")
        else:
            print("There's no such a player")

    # Launches all required for game methods (example creates first item's in item shop)
    def InitGame(self, player):
        print("Initializing the game")
        self.CreateFirstItems()
        self.CreateRooms()

        # Player will be in "Lobby" room
        player.actualRoom = self.rooms[0]
        self.ui_control.DrawMainMenu(player, self)

    def GetItemByName(self, itemName):
        for item in self.itemsInGame:
            if itemName == item.name:
                return item