class Trey:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plochad(self):
        print(f'площадь = {(self.a * self.b) / 2}')

    def peremetr(self):
        self.c = (self.a ** 2 + self.b ** 2) ** 0.5
        print(f'периметр = {self.a + self.b + self.c}')



tr1 = Trey(3, 5)
tr1.plochad()
tr1.peremetr()