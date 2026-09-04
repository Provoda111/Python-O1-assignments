import random

# This print command tells the user what is this program's purpose
print("Hei! Tämä ohjelma arpoo kokonaisluvun väliltä 1 - 10. Sinun tehtävä on arvata arpottu "
      + "kokonaisluku. Kerron sinulle, jos sinun kirjoitettu luku on liian suuri, liian pieni "
      + "tai oikein")

# Creates variable with random number 
randomNumber = random.randint(1, 10)
userInput = int(input("Kirjoita sinun arvaus:\n"))

while userInput != randomNumber:
    if userInput > randomNumber:
        print("Liian suuri arvaus")
    elif randomNumber > userInput:
        print("Liian pieni arvaus")
    elif randomNumber == userInput:
        print("Oikein!")
    userInput = int(input("Kirjoita sinun arvaus:\n"))