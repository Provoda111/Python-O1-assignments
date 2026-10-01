# import math
#
# luku1 = 100
# luku2 = 523
# 
# print(f"Luvun {luku1} logaritmi kannalla 10 on: ")
# print(f"{math.log10(luku1) :.2f}")
# print(f"{math.log10(luku2) :.2f}")

# ---------------------------
#luku = input("Hei! Kirjoita joku luku: \n")
#luku = int(luku)
# 
#if luku < 100:
#   print(f"Antamasi luku on {luku} ja on alle 100")
#elif luku > 100: 
#    print(f"Antamasi luku on {luku} ja on yli 100")
#else: 
#    print(f"Antamasi luku on {luku} ja on yhtäsuuri kuin 100")
# ---------------------------
#number = int(input("Hei! Kirjoita luku: \n"))
#
#if 10 <= number <= 20:
#    print(f"Sinun lukusi {number} on 10 ja 20 välillä")
#else:
#    print(f"Sinun lukusi {number} ei ole 10 ja 20 välissä")
# ---------------------------
#
#luku = 22
#
#if luku % 2 == 0:
#    print(f"Luku {luku} on parillinen")
#else:
#    print(f"Luku {luku} on pariton")
# ---------------------------
#kerta = 0
#
#while kerta < 20:
#    if (kerta % 2 == 0):
#        print()
#    else:
#        print(kerta)
#    kerta += 1
# ---------------------------
#
#import time
#
#userNumber = int(input("Kirjoita luku:\n"))
#print("")
#
#while userNumber >= 1:
#    print(userNumber)
#    time.sleep(userNumber)
#    userNumber -= 1
#    if userNumber == 0:
#        print("Kaboom!")
#        break
# ---------------------------
#password = "Bond"
#
#passwordInput = str(input("Kirjoita salasana:\n"))
#while passwordInput != password:
#    print("Väärä salasana, kokeile uudellen\n")
#    passwordInput = str(input("Kirjoita salasana:\n"))
#print("Oikea salasana, tervetuloa järjestelmään.")
# ---------------------------
#import random
#
#kolikko = random.randint(1,2)
#
#if kolikko == 1:
#    print("Kruunu")
#elif kolikko == 2:
#    print("Klaava")
# ---------------------------
#import random
#
#while True:
#    firstDice = random.randint(1,3)
#    secondDice = random.randint(1,3)
#    print(f"Ensimmäisen nopan arvo on {firstDice}")
#    print(f"Toisen nopan arvo on {secondDice}")
#    if firstDice == 3 and secondDice == 3:
#        print(f"Nyt tuli {firstDice} ja {secondDice}, jeej!")
#        break
#    else:
#        print(f"Nyt tuli {firstDice} ja {secondDice}, jatketaan")
# ---------------------------
#index = 20
#
#while True:
#    if index % 2 == 0:
#        print(index)
#    else:
#        print()
#    if index <= 0:
#        break
#    index -= 2
# ---------------------------
#userInput = ""
#
#while userInput != " ":
#    userInput = str(input("Mikä on sinun nimesi:\n"))
# ---------------------------
#names = ["Alice", "Bob", "Carmen",  "David", "Eve", "Fred", "George", "Harry", "Ivy", "Jill"]
#
#names.extend(["Michael", "Oliver"])
#
#print(type(names))
#
#if "Michael" in names:
#    print("Oho se on täällä")
#
#print(names[-1])
#print(names[-6:-10:-1]) # Start : Excluding : Step
#print(names[::]) # Prints full list
#print(names[::-1]) # Prints from last index to first index
#
#numbers = [3, 5, 10, 9]
#print(numbers[::])
#numbers.insert(2, 2)
#print(numbers[::])
#numbers.append(3)
#print(numbers[::])
#
#if 5 in numbers:
# Lisätty + 1 sille paikalle, koska ei käytetä missään pl. ohjelmoinnissa että joku on paikassa 0
#    print(f"Numero 5 on listan paikalla: {numbers.index(5) + 1}")
#    print("Lisätään numero 6 sen jälkeen")
#    numbers.insert(numbers.index(5) + 1, 6)
#    print(numbers)
#numbers.extend([15, 20])
#print(numbers)
# ---------------------------
#numbers = [1, 2, 3]
#newNumbers = []
#for number in numbers:
#    newNumbers.append(number * 2)
# ---------------------------
# Tämä ohjelma kysyy käyttäjältä
#
#usersFriendsName = []
#
#print("Jotta ohjelma loppuu pistä vaan välilyönti")
#
#while True:
#    userInput = str(input("Hei! Kirjoita sinun kaverisi nimi\n"))
#    if userInput == " ":
#        break
#    if len(userInput) >= 5:
#        usersFriendsName.append(str(userInput))
#    else:
#        print("Nimi on liian lyhyt, ei tuu listalle")
#
#if len(usersFriendsName) >= 1:
#    print(f"Sinulla on {len(usersFriendsName)} kaveria")
#print(usersFriendsName)
# ---------------------------
#kaverilista = []
#
#nimi = input("Kirjoita kaverisi nimi: ")
#
#while nimi != " ":
#    kaverilista.append(nimi)
#    nimi = input("Kirjoita kaverisi nimi: ")
#print(kaverilista)
# ---------------------------
#numbers = []
#for i in range(0, 21, 1):
#    numbers.append(i**2)
#print(numbers)
# ---------------------------
#def f(x):
#    print(x)
#    return 3
#print(f(2))
# ---------------------------
#timesToPrint = 10
#userFirstName = "James"
#
#def WriteName(name, timesToPrint):
#    for i in range(timesToPrint):
#        print(f"{name} {i + 1}. Kerta")
#WriteName(userFirstName, timesToPrint)
# ---------------------------
#tuple = (3, 5, 8, 10, (24, 25), "Moi", 200)
#tuple2 = (3, 5, 8, 10, (24, 25), "Moi", 200)
#
#print(f"Tuple:n pituus on: {len(tuple)}")
#print(tuple.index(10))
#if tuple.count(10):
#    print("There is number 10")
#else:
#    print("There is no number 10")
#if tuple.count(210):
#    print("There is number 210")
#else:
#    print("There is no number 210")
#for i in tuple:
#    print(i)
#print("-------------------------------------------")
#for i in tuple[::-1]:
#    print(i)
# ---------------------------

#numbers = {"Viivi":"050-1234567",
#           "Ahmed":"040-1112223",
#           "Pekka":"050-7654321",
#           "George":"040-75274572"}

#for person in numbers:
    #print(f"{person}:n puhelinnumero on {numbers[person]}")
#    print(f"{person}:n puhelinnumero on {numbers.get(person)}")

#userInput = str(input("Kirjoita kaverisi nimi: "))

#if userInput in numbers:
#    print(f"Listasta löytyi {userInput}. Kaverisi puhelinnumero on {numbers.get(userInput)}")
#else:
#    print("Valitettavasti nimi ei löytyny")

# ---------------------------
#
#students = [
#    {"name": "Ella", "age": 14, "grade": 9},
#    {"name": "Leo", "age": 15, "grade": 8},
#    {"name": "Aino", "age": 14, "grade": 10}
#]
#
#for student in students:
#    print(f"{student["name"]}:n arvo sana on {student["grade"]}")x

# ---------------------------
#class Person:
#    def __init__(self, name, surname, age):
#        self.name = name
#        self.surname = surname
#        self.age = age
#        pass
#
#    def walk(self):
#        print(f"{self.name} kävelee")
#
#    def CheckIfAdult(self):
#        if self.age >= 18:
#            return f"{self.name} on aikuinen"
#        else:
#            return f"{self.name} ei ole aikuinen"
#
#class Rectangle:
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width
#    
#    def Piiri(self):
#        return f"Suorakulmion piiri on: {(self.length * 2) + (self.width * 2)}"
#
#    def Pinta_Ala(self):
#        return f"Suorakulmion pinta-ala on {(self.length * 2) * (self.width * 2)}^2"
#
#class Book:
#
#    
#    def __init__(self, name, writer = "Tuntematon", pages = 100):
#        self.name = name
#        self.writer = writer
#        self.pages = pages   
#CrimeAndPunishment = Book("Crime and Punishment", "Someone")
#print(CrimeAndPunishment.pages)
#MetropoliaHistory = Book("Metropolia History", "Metropolia", 353)
#print(MetropoliaHistory.pages)
#Coding = Book("Coding on Python", "Someone cool", 493)


#person1 = Person("Matti", "Bond", 45)
#print(person1.CheckIfAdult())
#
#person2 = Person("James", "Bond", 15)
#print(person2.CheckIfAdult())
#
#r1 = Rectangle(5, 5)
#print(r1.Piiri())
#print(r1.Pinta_Ala())

# ---------------------------
#class Book:
#    def __init__(self, name):
#        self.name = name
#
#class Library:
#    def __init__(self, name, books = []):
#        self.name = name
#        self.books = books
#
#    def addBook(self, book):
#        self.books.append(book)
#        print(f"Lisättiin {book.name} kirjastoon")
#k1 = Book("Maila")
#k2 = Book("Tuntematon Sotilas")
#k3 = Book("Aakkoset")
#k4 = Book("Raamattu")
#kirjasto = Library("Oodi")
#kirjasto.addBook(k1)
#kirjasto.addBook(k2)
#kirjasto.addBook(k3)
#kirjasto.addBook(k4)
# ---------------------------
#class Muoto:
#    def __init__(self, color):
#        self.color = color
#
#    def Mittaa(self):
#        return "Nyt lasken piirin"
#
#class Rectangle(Muoto):
#    def __init__(self, color, length, width):
#        super().__init__(color)
#        self.length = length
#        self.width = width
#
#    def Mittaa(self):
#        print(super().Mittaa())
#        print(f"Piiri on {(self.length * 2) + (self.width * 2)}")
#
#rectangle = Rectangle("red", 3, 4)
#rectangle.Mittaa()
# ---------------------------
#while True:
#    try:
#        input = int(input("Kirjoita luku: "))
#        print("Jippii!!")
#        break
#    except:
#        print("Et kirjoittanut luvun")
# ---------------------------
print("4 8 15 16 23 42")

import Playlist

class Song:
    def __init__(self, singer = "Song doesn't have a singer", name = "Song doesn't have a name"):
        self.singer = singer
        self.name = name

s1 = Song("Metropolian students", "Metropolia anthem")
s2 = Song("KaMa members", "KaMa anthem")
s3 = Song("Python coders (no pls)", "Python bad song")
s4 = Song("Someone Idk", "Something Idk")
s5 = Song("C Sharpers", "C# has potential")
s6 = Song("Hardcoding", "Hardcoders")

songs = [s1, s2, s3]

spotify = Playlist.Playlist()

for song in songs:
    print(f"{song.singer} - {song.name}")
    spotify.AddSong(song)

# ---------------------------



# ---------------------------



# ---------------------------



# ---------------------------



# ---------------------------



# ---------------------------



# ---------------------------



# ---------------------------