# Tämä ohjelma kysyy käyttäjältä ympyrän säde ja tulostaa ympyrän pinta-ala, laskemalla
# x + y**2
# jossa x on luku pi, ja y on ympyrän säde

import math

radius = input("Kirjoita ympyrän säde: \n")

print(f"Ympyrän säde on {radius}")
print (f"Ympyrän pinta-ala on: {math.pi * int(radius)**2}")
