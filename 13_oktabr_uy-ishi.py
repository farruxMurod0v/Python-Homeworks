# class Mehmon:
#     def __init__(self, ism, yosh, kasb, email):
#         self.ism = ism
#         self.yosh = yosh
#         self.kasb = kasb
#         self.email = email
#     def print_mehmon(self):
#         print(f"Ismi: {self.ism}")
#         print(f"Yoshi: {self.yosh}")
#         print(f"Kasbi: {self.kasb}")
#         print(f"email: {self.email}")

# n_1 = Mehmon("Mayk Tayson", 65, "Bokschi", "@taysonN1@gmail.com")
# n_1.print_mehmon()



# class Meva:
#     def __init__(self, nomi, narxi, rang, kech_pishar):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.rang = rang
#         self.kech_pishar = kech_pishar
    
#     def about_meva(self):
#         print(f"Mevaning nomi: {self.nomi}")
#         print(f"Mevaning narxi: sum{self.narxi}")
#         print(f"Mevaning rangi: {self.rang}")
#         if self.kech_pishar == True:
#             print("Meva kech pishadi")
#         else:
#             print("Meva vaqtliroq pishadi")

# yozgi_meva = Meva(nomi="Xurmo", narxi=75000, rang="to'qsariq", kech_pishar=True)
# yozgi_meva.about_meva()




# class Hisob:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def qosh(self):
#         print("A va B sonning yig'indis = ")
#         print(self.a + self.b)
#         print()

#     def ayir(self):
#         print("A va B sondan ayirmasi = ")
#         print(self.a - self.b)
#         print("B dan A sondan ayirmasi = ")
#         print(self.b - self.a)
#         print()

#     def kop(self):
#         print("A va B sonning ko'paytmasi = ")
#         print(self.a * self.b)
#         print()
#     def qoldiq(self):
#         print("A sonnig B songa Bo'lgandagi qoldig'i = ")
#         print(self.a % self.b)
#         print("B sonnig A songa Bo'lgandagi qoldig'i = ")
#         print(self.b % self.a)


# h1 = Hisob(20, 468)
# h2 = Hisob(90, 879)
# n3 = Hisob(a=9854, b=78)
# h1.qosh()
# h2.ayir()
# h2.kop()
# n3.qoldiq()



# class Mashina:
#     def __init__(self, brend, narx, yil, tezlik, max_tezlik, uzunlik, balandlik, yuz, rang, popular, sport_rejim, gaz_benzin, elektr):
#         self.brend = brend
#         self.narx = narx
#         self.yil = yil
#         self.tezlik = tezlik
#         self.max_tezlik = max_tezlik
#         self.uzunlik = uzunlik
#         self.balandlik = balandlik
#         self.yuz = yuz
#         self.rang = rang
#         self.popular = popular
#         self.sport_rejim = sport_rejim
#         self.gaz_benzin = gaz_benzin
#         self.elektr = elektr

#     def show(self):
#         print(f"""brend = "{self.brend}",
#              narx = {self.narx},
#              yil = {self.yil},
#              max_tezlik = {self.max_tezlik},
#              uzunlik = {self.uzunlik},
#              balandlik = {self.balandlik},
#              rang = "{self.rang}",
#              gaz_benzin = "{self.gaz_benzin}",
#              elektr = "{self.elektr}",
#              popular = {self.popular},
#              yuz = {self.yuz},
#              sport_rejim = "{self.sport_rejim}",
#              tezlik = {self.tezlik}""")

#     def start(self):
#         if self.tezlik >= 20:
#             print("Mashina harakatlanyabdi, Xavfsizlik kamarlarini taqishni unutmang!!!")
#         else:
#             print("Mashina o't oldi ##")

#     def stop_car(self):
#         print("Avtamobil to'xtadi")
#         print("yetib keldik!!")

#     def tezlanish(self, a):
#         if (self.tezlik + a) != self.max_tezlik:
#             print(f"Mashina tezligi {a} tezlikka oshirildi")
#         else:
#             print("Masina tezligi 5 mp/h ga oshirildi")

#     def sekinlashish(self, sekin):
#         if (self.tezlik - sekin) != 0:
#             print(f"Mashina {sekin} mp/h ga sekinladi")
#         else:
#             print("Mashina sekinlashmadi")

#     def buril(self, left=False, right=False):
#         if left:
#             print("mashina chapga burildi")
#         if right:
#             print("Mashina o'ngga burildi")
#         else:
#             print("Hech qaysi tomonga burilish yo'q faqat oldinga boss")


# RR = Mashina(
#     brend="Phantom",
#     narx=450000,
#     yil=2022,
#     max_tezlik=300,
#     uzunlik=4,
#     balandlik=1.76,
#     rang="qora",
#     gaz_benzin="benzin",
#     elektr="yo'q",
#     popular=8.7,
#     yuz=5,
#     sport_rejim="sport rejim",
#     tezlik=70
# )

# RR.start()
# RR.buril(right=True)
# RR.sekinlashish(sekin=20)
# RR.tezlanish(a=100)
# RR.show()

class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def show_info(self):
        print(f"Ism: {self.ism}")
        print(f"Familiya: {self.familiya}")
        print(f"Yosh: {self.yosh}")

class Mijoz(Shaxs):
    def __init__(self, ism, familiya, yosh, telefon):
        super().__init__(ism, familiya, yosh)
        self.telefon = telefon

    def show_info(self):
        super().show_info()
        print(f"Telefon: {self.telefon}")

class Ishchi(Shaxs):
    def __init__(self, ism, familiya, yosh, lavozim):
        super().__init__(ism, familiya, yosh)
        self.lavozim = lavozim

    def show_info(self):
        super().show_info()
        print(f"Lavozim: {self.lavozim}")

class Menejer(Shaxs):
    def __init__(self, ism, familiya, yosh, bo'lim):
        super().__init__(ism, familiya, yosh)
        self.bolim = bolim

    def show_info(self):
        super().show_info()
        print(f"Bolim: {self.bolim}")


class Dasturchi(Shaxs):
    def __init__(self, ism, familiya, yosh, tillar):
        super().__init__(ism, familiya, yosh)
        self.tillar = tillar

    def show_info(self):
        super().show_info()
        print(f"Tillar: {self.tillar}")


shaxs1 = Mijoz("Ali", "Valiyev", 30, "123456789")
shaxs2 = Ishchi("Vali", "Aliyev", 25, "Direktor")
shaxs3 = Menejer("Hasan", "Huseynov", 35, "HR")
shaxs4 = Dasturchi("Alisher", "Karimov", 28, ["Python", "Java"])

shaxs1.show_info()
shaxs2.show_info()
shaxs3.show_info()
shaxs4.show_info()
