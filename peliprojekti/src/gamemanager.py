from player import Player
from ui import UI
from itemshop import ItemShop
from item import Item

class GameManager:
    ## TODO THINK ABOUT PLAYERS LIST
    def __init__(self):
        self.players = []
        self.ui_control = UI()
        self.itemShop = ItemShop()
        self.startRoom = None

    def LogIn(self):
        succesfullRegistration = False
        print("Let's start with creating your character")
        while succesfullRegistration != True:
            try:
                playerAgeInput = int(input("Kirjoita sinun ikäsi: "))
                playerNameInput = input("Kirjoita sinun nimesi: ")
                if playerAgeInput > 12 and playerNameInput != None and playerNameInput != "":
                    print("Account created succesfully")
                    succesfullRegistration = True
                else:
                    print("Can't create an account for you")
            except ValueError:
                print("Error in name or age input, try again")
        self.AddPlayer(playerNameInput, playerAgeInput)
            #except:
            #    print("Unknown error happened")
            
    def AddPlayer(self, playerNameInput, playerAgeInput):
        newPlayer = Player(playerNameInput, playerAgeInput)
        newPlayer.playerInfo = {
            "Name" : playerNameInput,
            "Age"  : playerAgeInput }
        self.players.append(newPlayer)
        self.InitGame(newPlayer)

    def DeletePlayer(self, targetPlayer):
        if targetPlayer in self.players:
            print(f"Deleting a player {targetPlayer["Name"]}")

    def CreateFirstItems(self):
        newItem = Item("Dagger", 25, "Cool melee weapon")
        self.itemShop.AddItemToShop(newItem)
        newItem = Item("Sword", 45, "Cool and strong melee weapon")
        self.itemShop.AddItemToShop(newItem)

    # Launches all required for game methods (example creates first item's in item shop)
    def InitGame(self, player):
        print("Initializing the game")
        self.CreateFirstItems()
        self.ui_control.DrawMainMenu(player, self)