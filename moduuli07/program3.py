airports = list()

def AddNewAirport():
    airport = dict()
    print('Valitsit lisätä uuden lentoaseman. ')
    cityInput = input("Kirjoita kaupunki, jossa lentoasema sijaitsee: ")
    ICAOInput = input("Kirjoita ICAO-koodi: ")
    nameInput = input("Kirjoita lentoaseman nimi: ")
    airport = {
            "City": cityInput,
            "ICAO": ICAOInput,
            "Name": nameInput
        }
    airports.append(airport)
    print("Lisätty uusi lentoasema")
def FindAirport():
    print("Valitsit hakea jo olevan lentoaseman")
    userInput = input("Kirjoita joko ICAO-Koodi, kaupungin tai nimen: ")
    if airports:
        for airport in airports:
            if airport["Name"] == userInput or airport["ICAO"] == userInput or airport["City"] == userInput:
                print(f"Lentoasema löyty, kirjoitan tiedot: Nimi: {airport.get("Name")}, "
                      + f"ICAO: {airport.get("ICAO")}, Kaupunki: {airport.get("City")}")
            else:
                print("Valitettavasti lentoasema ei löytynyt")
    else:
        print("Valitettavasti listassa ei ole yhtäkään lentoasemaa")

print("Hei! Tässä ohjelmassa kysyn sinulta lentoasemien tietoja (Kaupunki, ICAO-koodi ja nimi)")

while True:
    userInput = input("Mitä valitset:\n1 - Lisätä uuden lentoaseman\n2 - Hakea jo olevan\n3 - Lopeta\n")
    if userInput == "1" or userInput == "Lisää":
        AddNewAirport()
    if userInput == "2" or userInput == "Hakea":
        FindAirport()
    if userInput == "3" or userInput == "Lopeta":
        break