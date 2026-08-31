# Ohjelma kysyy käyttäjältä leiviskän, naulan ja luotien määrää
#Yksi leiviskä on 20 naulaa
# Yksi naula on 32 luotia
# Yksi luoti on 13,3 grammaa

playerInventoryWeight = 0.0
bulletWeight = 13.3
totalBulletAmount = 0.0

bulletAmount = float(input("Kirjoita luotien määrää: \n"))
totalBulletAmount += bulletAmount

leiviskaAmount = float(input("Kirjoita leiviskien määrää: \n"))
leiviskaForNail = 20

nailAmount = float(input("Kirjoita naulojen määrää: \n")) + leiviskaAmount * leiviskaForNail
nailForBullet = 32
totalBulletAmount += nailAmount * nailForBullet



playerInventoryWeight += bulletAmount * bulletWeight
print(playerInventoryWeight)
