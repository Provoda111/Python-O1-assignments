names = set()
while True:
    userInput = input("Kirjoita nimi: ")

    if userInput in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        names.add(userInput)
        
    if userInput == " ":
        print("Kirjoitan kaikki syötetyt nimet:")
        for name in names:
            print(name)
        break