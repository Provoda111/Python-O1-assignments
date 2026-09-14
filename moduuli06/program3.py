litersToGallon = 3.785

def ReturnLiterAmount(gallon):
    return f"{gallon} gallon is {gallon * litersToGallon} liter"

userLiterInput = input("Write how much gallons you want to convert to liters: ")
print(ReturnLiterAmount(float(userLiterInput)))
