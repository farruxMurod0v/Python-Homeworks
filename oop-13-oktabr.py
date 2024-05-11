import math

class Hisob:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def qosh(self):
        self.a = self.a + self.b
        self.b = self.b + self.a

    def ayir(self):
        self.a = self.a - self.b
        self.b = self.b - self.a

    def kop(self):
        self.a = self.a * self.b
        self.b = self.b * self.a

    def gacha_kop(self):
        fac = 1
        for i in range(self.b):
            fac *= self.a
        return fac

    def summa(self):
        s = 0
        for i in range(self.b):
            s += self.a
        return s

    def qoldiq(self):
        self.a = self.a % self.b
        self.b = self.b % self.a

    def daraja(self):
        self.a = math.pow(self.a, self.b)
        self.b = math.pow(self.b, self.a)

h1 = Hisob(20, 468)
h2 = Hisob(90, 879)
h1.daraja()