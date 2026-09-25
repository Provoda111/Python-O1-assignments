months = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu",
          "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

print("Hello, you should write a month (number) and i'll tell is it in finnish kevät, kesä, syksy, talvi")
userInput = int(input("Anna kuukauden numero (1 - 12): "))
month = months[userInput - 1]
print(f"{month}")