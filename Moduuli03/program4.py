print("Hei! Tämä ohjelma kysyy käyttäjältä vuosiluvun ja ilmoittaa, onko annettu vuosi "
      + "karkausvuosi.")
userYearInput = int(input("Kirjoita vuosiluku:\n"))

if (userYearInput % 4 == 0 and userYearInput % 100 != 0) or (userYearInput % 400 == 0):
    print(f"Antamasi vuosiluku ({userYearInput}) on karkausvuosi")
else:
    print(f"Antamasi vuosiluku ({userYearInput}) ei ole karkausvuosi")