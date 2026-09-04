print("Hei! Tämä ohjelma muuntaa tuumia senttimetreiksi niin kauan kunnes"
+ " käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa")

inchInput = float(input("Kirjoita kuinka monta tuumaa:\n"))

while inchInput >= 0:
    print(f"Annoit {inchInput} tuuma. Senttimetreinä se on {inchInput * 2.54}")
    inchInput = float(input("Kirjoita kuinka monta tuumaa:\n"))