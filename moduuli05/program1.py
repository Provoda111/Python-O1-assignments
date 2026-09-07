# Ohjelma kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpa-
# kuutioita ja tulostaa silmälukujen summan. Ohjelmassa käytetään for-toistorakennetta

import random


throwDiceAmount = int(input("Kirjoita kuinka monta kertaa minun pitäisi heittaa nopan:\n"))
diceNumberSum = 0


for i in range(throwDiceAmount):
    print("Heitän nopan.............")
    throwDiceAmount -= 1
    throwedDice = random.randint(1, 6)
    diceNumberSum += throwedDice
    print(f"Tippui numero {throwedDice}")
    print(f"Meillä jäi vielä heittämättä {throwDiceAmount}")
print(f"Sinulla tippui nopasta yhteenlaskettuna {diceNumberSum}")