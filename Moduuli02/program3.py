# Tämä ohjelma kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-ala. 

print("Hei! Lasken sinun puolesta suorakulmion kannan ja korkeuden.")
rectangleBase = input("Kirjoita suorakulmion kanta: \n")
rectangleHeight = input("Kirjoita suorakulmion korkeuden: \n")

print(f"Suorakulmion piiri on: {int(rectangleBase) * 2 + int(rectangleHeight) * 2}")
print(f"Suorakulmion pinta-ala on: {int(rectangleBase) * int(rectangleHeight)}")