# Ohjelma kysyy käyttäjältä kolme kokonaislukua
# Ja laskee niiden summan, tulon ja keskiarvon

import statistics

print("Hei! Kirjoita minulle kolme kokonaislukua ja minä lasken sinun puolesta" \
"Niiden summman, tulon ja keskiarvon")

number1 = input("Kirjoita ensimmäisen luvun: \n")

number2 = input("Kirjoita toisen luvun: \n")

number3 = input("Kirjoita kolmannen luvun: \n")

print(f"Sinun kirjoittamien luvun summa on: {int(number1) + int(number2) + int(number3)}")
print(f"Sinun kirjoittamien luvun tulo on: {int(number1) * int(number2) * int(number3)}")
numbers = [int(number1), int(number2), int(number3)]
ka = statistics.mean(numbers)
print(f"Sinun kirjoittamien luvun tulo on: {ka :.2f}")
