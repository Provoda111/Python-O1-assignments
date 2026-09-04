print("Hei! Tervetuloa sisäänkirjautumis ohjelmaan. Jotta sinä pääset järjestelmään sinun "
      + "pitää kirjoittaa oikein käyttäjätunnus ja salasana.")

username = "python" # Creates and sets value for variable "username" a "python" 
userPassword = "rules" # Creates and sets value for variable "userPassword" a "rules"
# Creates an empty string variable for future interaction. 
usernameInput = "" 
userPasswordInput = ""
attemptsToLog = 5

while usernameInput != username or userPasswordInput != userPassword:
    usernameInput = str(input("Kirjoita käyttäjänimi:\n"))
    userPasswordInput = str(input("Kirjoita salasana:\n"))

    if usernameInput != username or userPasswordInput != userPassword:
        attemptsToLog -= 1
        print("Pääsy evätty")
        print(f"Jäljellä olevat yritykset {attemptsToLog}")
    else:
        print("Tervetuloa")
    if attemptsToLog <= 0:
        print("Sinulla ei ole enään mahdollisuuksia yrittää kirjautua sisään. Pahoittelemme")
        break