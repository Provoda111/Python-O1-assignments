# Ohjelma kysyy käyttäjältä lukuja siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon lopetus-
# merkiksi. Lopuksi ohjelma tulostaa käyttäjälle saaduista luvuista viisi suurinta suurusjärjestykse-
# ssä

numbers = []

print("Jos haluat, että ohjelma keskeytyy, pistä välilyönti syöttökentälle")

while True:
    userInput = input("Kirjoita jokin kokonaisluku: ")
    if userInput == " ":
        break
    numbers.append(int(userInput))
    
numbers.sort(reverse=True)
print(numbers)