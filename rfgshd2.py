class Kvadrat:

    def __init__(self, a):
        self.a = a

    def plochad(self):
        print(f'площадь = {self.a * 4}')

    def peremeter(self):
        print(f'периметр = {self.a * 2}')






kd1 = Kvadrat(5)
kd1.plochad()
kd1.peremeter()