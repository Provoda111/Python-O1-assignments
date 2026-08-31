print("Hei! Kirjoita haluamasi hyttiluokka. Valitse LUX, A, B vai C luokka")
userHytti = str(input("Minkä valitset? \n"))

if userHytti == "LUX" or userHytti == "lux":
    print(f"Valitsit LUX hyttiluokan. LUX on parvekkeellinen hytti yläkannella.")
elif userHytti == "A" or userHytti == "a":
    print("Valitsit A hyttiluokan. A on ikkunallinen hytti autokannen yläpuolella.")
elif userHytti == "B" or userHytti == "b":
    print("Valitsit B hyttiluokan. B on ikkunaton hytti autokannen yläpuolella.")
elif userHytti == "C" or userHytti == "c":
    print("Valitsit C hyttiluokan. C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")