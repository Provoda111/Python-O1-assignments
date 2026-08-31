maximumMenHemoglobin = int(175)
minimunMenHemoglobin = int(117)

maximumWomenHemoglobin = int(195)
minimunWomenHemoglobin = int(134)

print("Hei!")

userGender = str(input("Kirjoita sinun sukupuolisi (Mies/Nainen):\n"))
userHemoglobin = int(input("Kirjoita sinun hemoglobiiniarvosi:\n"))

if userGender == "Mies":
    if userHemoglobin > maximumMenHemoglobin:
        print("Sinun hemoglobiini arvo on suurempi kuin pitäisi olla.")
        print(f"Lääkärien suositus on {maximumMenHemoglobin} g/l")
    elif userHemoglobin < minimunMenHemoglobin:
        print("Sinun hemoglobiini arvo on pienempi kuin pitäisi olla.")
        print(f"Lääkärien suositus on {minimunMenHemoglobin} g/l")
    elif minimunMenHemoglobin <= userHemoglobin <= maximumMenHemoglobin:
        print("Sinun hemoglobiini arvo on normaali!")
elif userGender == "Nainen":
    if userHemoglobin > maximumWomenHemoglobin:
        print("Sinun hemoglobiini arvo on suurempi kuin pitäisi olla.")
        print(f"Lääkärien suositus on {maximumWomenHemoglobin} g/l")
    elif userHemoglobin < minimunWomenHemoglobin:
        print("Sinun hemoglobiini arvo on pienempi kuin pitäisi olla.")
        print(f"Lääkärien suositus on {minimunWomenHemoglobin} g/l")
    elif minimunWomenHemoglobin <= userHemoglobin <= maximumWomenHemoglobin:
        print("Sinun hemoglobiini arvo on normaali!")
else:
    print("Kuka sinä olet???")