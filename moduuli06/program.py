import random

print("Hello! This program throws a dice, and tells you the result, but to win the result must be "
      + "a number 6")

def ThrowDice():
    diceNumber = random.randint(1, 6)
    while diceNumber != 6:
        print(f"I throwed an dice and you got {diceNumber}")
        if diceNumber == 6: 
            print(f"You've got a number 6! You won!")
            break
        diceNumber = random.randint(1, 6)

ThrowDice()