print("Hei! Tämä ohjelma kysyy käyttäjältä lukuja siihen saakka, kunnes syötät tyhjän "
      + "merkkijonon lopetusmerkiksi")

userInput = 0
numbersFromUser = []

while userInput != " ":
    userInput = input("Kirjoita kokonaisluku:\n")
    if int(userInput):
        numbersFromUser.append(int(userInput))
        numbersFromUser.sort()
else:
    index = 0
    while index <= len(numbersFromUser):
        print(numbersFromUser[index])
        index += 1
    