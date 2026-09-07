howMuchTimeToAsk = 5
cities = []

for i in range(howMuchTimeToAsk):
    userInput = input("Hei! Kirjoita sinun lempparit kaupungit (Ainoastaan viisi):\n")
    cities.append(userInput)
print("Kiitos vastauksesta, sinulla on hyvä kaupunkien valinta.")

for i in cities:
    print(f"Kaupunki {cities.index(i) + 1} - {i}")