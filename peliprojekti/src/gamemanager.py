from player import Player
from ui import UI
from itemshop import ItemShop

class GameManager:
    ## TODO THINK ABOUT PLAYERS LIST
    def __init__(self):
        self.players = []
        self.ui_control = UI()
        self.itemShop = ItemShop()

    def LogIn(self):
        print("Let's start with creating your character")
        while True:
            try:
                playerAgeInput = int(input("Kirjoita sinun ikäsi: "))
                playerNameInput = input("Kirjoita sinun nimesi: ")
                if playerAgeInput > 12 and playerNameInput != None and playerNameInput != "":
                    print("Account created succesfully")
                    self.AddPlayer(playerNameInput, playerAgeInput)
                    break
                else:
                    print("Can't create an account for you")
            except ValueError:
                print("Error in name or age input, try again")
            except:
                print("Unknown error happened")
            
    def AddPlayer(self, playerNameInput, playerAgeInput):
        newPlayer = Player(playerNameInput, playerAgeInput)
        newPlayer.playerInfo = {
            "Name" : playerNameInput,
            "Age"  : playerAgeInput }
        self.players.append(newPlayer)
        self.StartGame(newPlayer)

    def DeletePlayer(self, targetPlayer):
        if targetPlayer in self.players:
            print(f"Deleting a player {targetPlayer["Name"]}")

    def StartGame(self, player):
        print("Starting the game")
        self.ui_control.DrawMainMenu(player, self)