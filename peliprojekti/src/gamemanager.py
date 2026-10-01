from player import Player
from ui import UI
from itemshop import ItemShop
from item import Item
from room import Room


# GameManager luokan (ja itse tiedoston) tehtävänä on järjestää muiden luokkien vuorovaikutusta, kutsumalla tietyt funktiot
# Käyttäen toisten luokkien arvot jne. GameManager on ainoa luokka jossa asetetaan yhteiset arvot muuttujille, jota muut luokat ja
# Tiedostot käyttävät
class GameManager:
    
    def __init__(self):
        self.players = []
        self.ui_control = UI()
        self.itemShop = ItemShop()
        self.startRoom = None
        self.rooms = tuple()
        self.itemsInGame = []

    # Creates a player character to the game
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
        self.itemsInGame.append(newItem)
        newItem = Item("Sword", 45, "Cool and strong melee weapon")
        self.itemShop.AddItemToShop(newItem)
        self.itemsInGame.append(newItem)
    
    def CreateRooms(self):
        tmpList = list(self.rooms)
        tmpList.extend([Room("Lobby", "First room in castle", "L", False), Room("Visitor's bedroom", "Visitors can sleep here", "VB1", False), Room("Main bedroom", "There is a story, that here is sleeping prince of the castle", "MB1", False), Room("Armory", "Here is all weapons of this castle", "A", False), Room("Throne", "King is here", "Thr", True)])
        self.rooms = tuple(tmpList)
        pass

    # Launches all required for game methods (example creates first item's in item shop)
    def InitGame(self, player):
        print("Initializing the game")
        self.CreateFirstItems()
        self.CreateRooms()
        player.actualRoom = self.rooms[3]
        self.ui_control.DrawMainMenu(player, self)