# Tämä ohjelma arpoo ja tulostaa käyttäjälle kaksi erilaista numerolukon koodia

import random

code_tmp = ""

for luku in range(3):
    randomThreeCode = str(random.randint(0, 9))
    code_tmp += randomThreeCode
print(f"Arposin kolmenumeroisen koodin: {code_tmp}")

code_tmp = ""

for luku in range(4):
    randomFourCode = str(random.randint(1, 6))
    code_tmp += randomThreeCode
print(f"Arposin nelinumeroisin koodin: {code_tmp}")