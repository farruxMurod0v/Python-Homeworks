# class Shape:
#     nom = ""
#     def area(self):
#         raise NotImplementedError("Yuza hisoblash "
#                                   "metodi kiritilmagan")
#     def perim(self):
#         raise NotImplementedError("Perimetr hisoblash "
#                                   "metodi kiritilmagan")

# class Circle(Shape):
#     radius = 32
#     def area(self):
#         p = 3.14
#         area = p * self.radius **2
#         return area

# class Rect(Shape):
#     a, b = 8, 10
#     def area(self):
#         area = self.a * self.b
#         return area
#     def perim(self):
#         perim = (self.a + self.b) * 2
#         return perim

# class Tri(Shape):
#     a, b, c = 96, 74, 41

#     def perim(self):
#         p = self.a + self.b + self.c
#         return p

# uch = Tri()




class Mashina:
    def __init__(self, brend, narx, yil, tezlik, max_tezlik, uzunlik, balandlik, yuz, rang, popular, sport_rejim, gaz_benzin, elektr):
        self.brend = brend
        self.narx = narx
        self.yil = yil
        self.tezlik = tezlik
        self.max_tezlik = max_tezlik
        self.uzunlik = uzunlik
        self.balandlik = balandlik
        self.yuz = yuz
        self.rang = rang
        self.popular = popular
        self.sport_rejim = sport_rejim
        self.gaz_benzin = gaz_benzin
        self.elektr = elektr

    def show(self):
        print(f"""brend = "{self.brend}",
             narx = {self.narx},
             yil = {self.yil},
             max_tezlik = {self.max_tezlik},
             uzunlik = {self.uzunlik},
             balandlik = {self.balandlik},
             rang = "{self.rang}",
             gaz_benzin = "{self.gaz_benzin}",
             elektr = "{self.elektr}",
             popular = {self.popular},
             yuz = {self.yuz},
             sport_rejim = "{self.sport_rejim}",
             tezlik = {self.tezlik}""")

    def start(self):
        if self.tezlik >= 20:
            print("Mashina harakatlanyabdi, Xavfsizlik kamarlarini taqishni unutmang!!!")
        else:
            print("Mashina o't oldi ##")

    def stop_car(self):
        print("Avtamobil to'xtadi")
        print("yetib keldik!!")

    def tezlanish(self, a):
        if (self.tezlik + a) != self.max_tezlik:
            print(f"Mashina tezligi {a} tezlikka oshirildi")
        else:
            print("Masina tezligi 5 mp/h ga oshirildi")

    def sekinlashish(self, sekin):
        if (self.tezlik - sekin) != 0:
            print(f"Mashina {sekin} mp/h ga sekinladi")
        else:
            print("Mashina sekinlashmadi")

    def buril(self, left=False, right=False):
        if left:
            print("mashina chapga burildi")
        if right:
            print("Mashina o'ngga burildi")
        else:
            print("Hech qaysi tomonga burilish yo'q faqat oldinga boss")


RR = Mashina(
    brend="Phantom",
    narx=450000,
    yil=2022,
    max_tezlik=300,
    uzunlik=4,
    balandlik=1.76,
    rang="qora",
    gaz_benzin="benzin",
    elektr="yo'q",
    popular=8.7,
    yuz=5,
    sport_rejim="sport rejim",
    tezlik=70
)

class samalyut (Mashina):
    def __init__(self, brend, narx, yil, tezlik, max_tezlik, uzunlik, balandlik, yuz, rang, popular,
                  sport_rejim, gaz_benzin, elektr):
        super().__init__(brend, narx, yil, tezlik, max_tezlik, uzunlik, balandlik, yuz, rang, popular,
                          sport_rejim, gaz_benzin, elektr)
        
    def start(self):
        return super().start()
    def tezlanish(self, a):
        return super().tezlanish(a)
    def buril(self, left=False, right=False):
        return super().buril(left, right)
    def stop_car(self):
        return super().stop_car()
    def sekinlashish(self, sekin):
        return super().sekinlashish(sekin)
    
qiruvchu_n1 = samalyut()
qiruvchu_n1