class Reader:
    def __init__(self, fio, ticketNum, fac, bigthDate, phone):
        self.fio = fio
        self.ticketNum = ticketNum
        self.fac = fac
        self.bightDate = bigthDate
        self.phone = phone

    def takeBook(self):
        self.koloBooks = input(f"Сколько книг должен взять {self.fio}?\n")
        print(f'{self.fio} взял {self.koloBooks} книг')

    def returnBook(self):
        print(f'{self.fio} вернул {self.koloBooks} книг')


person = Reader('Петров.В.В', '12', 'python', '05.12.2007', '01239412')
person.takeBook()

person.returnBook()
