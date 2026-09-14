numbers = []

for i in range(4):
    userInput = int(input("Write a number: "))
    numbers.append(userInput)

def SumListNumbers(list):
    print("I will sum all of your numbers that you've writed to me")
    print("Result is:")
    numbersSum = 0
    for number in list:
        numbersSum += number
    return numbersSum

print(SumListNumbers(numbers))