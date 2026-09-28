# Julkaisu
class Publication:
    def __init__(self, name):
        self.name = name


# Kirja
class Book(Publication):
    def __init__(self, name, writer, pageAmount):
        super().__init__(name)
        self.writer = writer
        self.pageAmount = pageAmount
    def Info(self):
        return f'Book "{self.name}", Writer - {self.writer}, {self.pageAmount} pages'

# Lehti
class Magazine(Publication):
    def __init__(self, name, chiefEditor):
        super().__init__(name)
        self.chiefEditor = chiefEditor
    def Info(self):
        return f'Magazine "{self.name}" Chief Editor - {self.chiefEditor}'

akuAnkka = Magazine("Aku Ankka", "Aki Hyyppä")
book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)
print(book1.Info())
print(akuAnkka.Info())