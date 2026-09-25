names = set()
while True:
    userInput = input("Kirjoita nimi: ")
    if userInput == " ":
            print("Kirjoitan kaikki syötetyt nimet:")
            for name in names:
                print(name)
            break
    if userInput in names:
        print("Aiemmin syötetty nimi\n")
    else:
        print("Uusi nimi\n")
        names.add(userInput)

def Jotain():
    pass