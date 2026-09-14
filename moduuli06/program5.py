numbers = [1, 4, 5, 7, 9, 10, 12, 13]

def RemoveOddNumbers(list):
    evenNumbers = []
    for number in list:
        if number % 2 == 0:
            evenNumbers.append(number)
    print("I've succesfully created a new list and inserted into it evenNumbers")
    return f"Your first list contains these numbers: {list}\n New list contains these numbers: {evenNumbers}"

print(RemoveOddNumbers(numbers))

