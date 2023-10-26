class Phone:
    def __init__(self, number, model, weight, name):
        self.number = number
        self.model = model
        self.weight = weight
        self.name = name

    def receivePhone(self):
        print(f'Звонит {self.name}')

    def getNumber(self):
        print(self.number)


phone1 = Phone('132231432', 'Iphone', 0.19, 'Радик')
phone2 = Phone('243561421', 'Redmi', 0.28, "Ваня")
phone3 = Phone('143253132', 'Sumsung', 0.1, "Николай")

phone1.receivePhone()
phone1.getNumber()
phone2.receivePhone()
phone2.getNumber()
phone3.receivePhone()
phone3.getNumber()
