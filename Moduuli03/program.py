fishMinimunLength = 37.0

print("Hei!")
fishLength = float(input("Kirjoita kuhan pituuden senttimetreinä:\n"))
if fishLength <= fishMinimunLength:
    print("Laske kuha takaisin järveen. Kuha on alimittainen.")
    print(f"Kuha on alimittainen, jos kuhan pituus on vähempi kuin {fishMinimunLength} cm")
    print(f"Löydä kuha joka on {fishMinimunLength - fishLength} cm pidempi")
else