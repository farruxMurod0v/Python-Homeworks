# class Talaba:
#     def __init__(self, ism, yosh, bahosi, guruh, kurs):
#         self.ism = ism
#         self.yosh = yosh
#         self.bahosi = bahosi
#         self.guruh = guruh
#         self.kurs = kurs

#     def __repr__(self):
#         return f"Talaba: {self.ism}, Yosh: {self.yosh}, Bahosi: {self.bahosi}, Guruhi: {self.guruh}, Kursi: {self.kurs}"

#     def update_yosh(self):
#         num = int(input("Talabalar yoshiga qo'shmoqchi bo'lgan soningizni kiriting: "))
#         if num + self.yosh > 0:
#             self.yosh += num
#         else:
#             print("Talabani talabaga qo'shib bo'lmaydi")
        
# talabalar = [
#     Talaba("Ali", 20, 90, "A", 1),
#     Talaba("Vali", 19, 85, "B", 3),
#     Talaba("Hasan", 21, 95, "A", 4),
#     Talaba("Husan", 18, 80, "C", 4),
#     Talaba("Soli", 22, 92, "A", 2),
#     Talaba("Abbos", 29, 88, "B", 1),
#     Talaba("Jasur", 16, 87, "B", 2),
#     Talaba("Dumbul", 25, 91, "A", 4),
#     Talaba("Sarvar", 17, 83, "C", 3),
#     Talaba("Sunnat", 24, 89, "B", 3)
# ]

# sorted_talabalar = sorted(talabalar, key=lambda talaba: talaba.kurs)
# for talaba in sorted_talabalar:
#     print(talaba)

# num = talabalar[0].update_yosh()
# print(num)
# print(talabalar)













# class Vehicle:
#     def fuel_efficiency(self):
#         pass

# class Car(Vehicle):
#     def fuel_efficiency(self):
#         return "Car fuel efficiency is 20 km/l"

# class Motorcycle(Vehicle):
#     def fuel_efficiency(self):
#         return "Motorcycle fuel efficiency is 30 km/l"

# car = Car()
# motorcycle = Motorcycle()

# print(car.fuel_efficiency())
# print(motorcycle.fuel_efficiency())
# class videokarta:
#     def __init__(self):
#         self.a = []

#     def update_list(self):
#         num = int(input("Listga qo'shmoqchi bo'lgan soningizni kiriting: "))
#         self.a.append(num)
#         return self.a
    
# v1 = videokarta()
# v1.update_list()
# print(v1.a)






# class Videokarta:
#     def init(self):
#         self.a = [0]*20

#     def add(self, other):
#         self.a = [i+other for i in self.a]
#         return self.a

# V1 = Videokarta()
# print(V1+5)
# print(V1+5)







# class Videokarta:
#     def __init__(self):
#         self.a = [0] * 20

#     def update_list(self, num):
#         for i in range(len(self.a)):
#             self.a[i] += num
#         return self.a
    
# v1 = Videokarta()
# v1.update_list(5)
# print(v1.a)




# class Animal:
#     def __init__(self, name, year, tirik, vazn):
#         self.name = name
#         self.year = year
#         self.tirik = tirik
#         self.vazn = vazn

#     def taom(self):
#         print("Taomlanish.. Xam xam")

#     def ovoz(self):
#         raise NotImplementedError("Ovoz methodini yaratmadingiz.")

#     def show(self):
#         print(f"Otim {self.name}")
#         print(f"Yoshim {2023-self.year}")
#         print(f"{self.vazn} kiloman")


# class Cat(Animal):
#     def __init__(self, name, year, tirik, vazn):
#         super().__init__(name, year, tirik, vazn)

#     def ovoz(self):
#         print("Myau myau mau")
#         print("Myau myau mau")


# class Dog(Animal):
#     def __init__(self, name, year, tirik, vazn):
#         super().__init__(name, year, tirik, vazn)

#     def ovoz(self):
#         print("Vov vov vov")
#         print("Vov vov vov")

# class Cow(Animal):
#     def __init__(self, name, year, tirik, vazn):
#         super().__init__(name, year, tirik, vazn)

#     def ovoz(self):
#         print("mu  mu - u")
#         print("moo mu")


# a = Cat("Baroqvoy", 2022, True, 3.5)
# b = Dog("Olapar", 2021, True, 10)
# gomish = Cow("Masha", 2000, True, 25)
# gomish.ovoz()
# a.ovoz()

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
#         print(area)
#         return area

# class Rect(Shape):
#     a, b = 8, 10
#     def area(self):
#         area = self.a * self.b
#         print(area)
#         return area
#     def perim(self):
#         perim = (self.a + self.b) * 2
#         print(perim)
#         return perim
        

# class Tri(Shape):
#     a, b, c = 96, 74, 41

#     def perim(self):
#         p = self.a + self.b + self.c
#         print(p)

# uch = Tri()
# uch.perim()
# t = Rect()
# t.area()



# class Vehicle:
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         print("Starting car engine...")

# class Motorcycle(Vehicle):
#     def start_engine(self):
#         print("Starting motorcycle engine...")

# car = Car()
# motorcycle = Motorcycle()
# car.start_engine()  
# motorcycle.start_engine()



# class Music:
#     def __init__(self, nom, yil, rang, vazn):
#         self.nom = nom
#         self.yil = yil
#         self.rang = rang
#         self.vazn = vazn

#     def ovoz(self):
#         raise NotImplementedError("ovoz methodini yaratmadingiz.")

#     def show(self):
#         print(f"nomi: {self.nom}")
#         print(f"Ishlab chiqarilgan yili: {self.yil}")
#         print(f"rangi: {self.rang}")
#         print(f"og'irligi: g{self.vazn}")
        


# class nay(Music):
#     def __init__(self,  nom, yil, rang, vazn):
#         super().__init__(nom, yil, rang, vazn)

#     def ovoz(self):
#         print("----")

# class baraban(Music):
#     def __init__(self,  nom, yil, rang, vazn):
#         super().__init__(nom, yil, rang, vazn)

#     def ovoz(self):
#         print("dub ---- dub ")
       
# a = nay("nay", 1600, "qizil", 200)
# a.show()
# b = baraban("baraban katta", 1876, "jigarrang", 150)
# b.show()



class calculate:
    def __init__(self, soat, maosh) -> None:
        self.soat = soat 
        self.maosh = maosh
        self.javob = self.soat * self.maosh

class Manager(calculate):
    def __init__(self, soat, maosh, ism, kun) -> None:
        super().__init__(soat, maosh)
        self.ism = ism
        self.kun = kun
    def get_maosh(self):
        return f"{self.ism}, Maoshi: ${self.javob * (self.kun * 4)}"
    
ali = Manager(6, 60, "KADIROv", 4)
print(ali.get_maosh())
       