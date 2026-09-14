import math

pizza1Diameter = float(input("Kirjoita ensimmäisen pizzan halkaisija: "))
pizza1Price = float(input("Kirjoita ensimmäisen pizzan hinta: "))
pizza2Diameter = float(input("Kirjoita toisen pizzan halkaisija: "))
pizza2Price = float(input("Kirjoita toisen pizzan hinta: "))


def CountBestPizza(Pizza1Diameter, Pizza1Price, Pizza2Diameter, Pizza2Price):
    pizza1Area = pizza1Diameter * math.pi
    pizza2Area = pizza2Diameter * math.pi

    pizza1PricePerArea = pizza1Area / pizza1Price
    pizza2PricePerArea = pizza2Area / pizza2Price

    print(f"Ensimmäisen pizzan hinta per 1 neliömetri: {pizza1PricePerArea:2f}")
    print(f"Toisen pizzan hinta per 1 neliömetri: {pizza2PricePerArea:3f}")
    if pizza1PricePerArea < pizza2PricePerArea:
        return f"Toinen pizza on parempi, koska pizzan hinta on kohtuullinen kokoon ottaen"
    elif pizza2PricePerArea < pizza1PricePerArea:
        return f"Ensimmäinen pizza on parempi, koska pizzan hinta on kohtuullinen kokoon ottaen"
    elif pizza2PricePerArea == pizza1PricePerArea:
        return f"Ensimmäinen ja toinen pizza ovat samanlaisia pizzan hinta kokoon ottaen"

print(CountBestPizza(pizza1Diameter, pizza1Price, pizza2Diameter, pizza2Price))