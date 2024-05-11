

#1
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
#         __p = 3.14
#         __area = __p * self.radius **2
#         print(__area)
#         return __area

# class Rect(Shape):
#     a, b = 8, 10
#     def area(self):
#         __area = self.a * self.b
#         print(__area)
#         return __area
#     def perim(self):
#         __perim = (self.a + self.b) * 2
#         print(__perim)
#         return __perim
        

# class Tri(Shape):
#     a, b, c = 96, 74, 41

#     def perim(self):
#         __perim = self.a + self.b + self.c
#         print(__perim)

# uch = Tri()
# uch.perim()
# t = Rect()
# t.area()






# #2

# class User:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def show_details(self):
#         return f"Thank you, {self.age} years old, {self.name.title()}"
    
# class Bank(User):
#     total_deposits = 0
#     total_withdraws = 0

#     def __init__(self, name, age, balance) -> None:
#         super().__init__(name, age)
#         self.balance = balance

#     def show_info(self):
#         return f"{self.name} has a remaining balance of: ${round(self.balance, 2)}"
    
#     def deposit(self):
#         dp = float(input(f"{self.name.title()}, pleace enter how much you would like to deposit? "))
#         print("Thank ypu depositing... ")
#         self.balance += dp
#         self.total_deposits += 1
#         return f"Your balance is now: {round(self.balance, 2)}"
    
#     def withdraws(self):
#         wd =  float(input(f"{self.name.title()}, pleace enter how much you would like to withdraw? "))
#         if self.balance < wd:
#             return "YOU can't withdraw that amount"
#         else: 
#             print("Thank you for withdrawing...")
#             self.balance -= wd 
#             self.total_withdraws += 1

#     def options(user_two):
#         print("Thank you creating your bank account")
#         print("Here are a list of options pleace choose the number you want ... ")
#         while True:
#             option_choice = int(input("1) See Balance\n 2) Withdraw\n 3) Deposit\n 4) See Total Withdraws\n 5) See Total Deposits\n 6) Quit\n"))

#             if option_choice == 1:
#                 print(user_one_bank.show_info())
#                 if option_choice == 1 and user_two != None:
#                     print(user_two_bank.show_info())
            
#             elif option_choice == 2:
#                 print(user_one_bank.withdraws())
#                 if option_choice == 2 and user_two != None:
#                     wd = input(f"{user_two.name} would you like withdraw? Yes or No? ")
#                     if wd.lower() == 'yes':
#                         print(user_two_bank.withdraws())
#             elif option_choice == 3:
#                 print(user_one_bank.deposit())
#                 if option_choice == 3 and user_two != None:
#                     dep = input(f"{user_two.name} would you like deposit ? Yes or No ")
#                     if dep.lower() == 'yes':
#                         print(user_two_bank.deposit())
#             elif option_choice == 4:
#                 print(f"There have been {user_two_bank.total_whithdraws} withdraws. ")
#                 if option_choice == 4 and user_two != None:
#                     print(f"There have been {user_two_bank.total_withdraws} withdraws. ")
#             elif option_choice == 5:
#                 print(f"There have been {user_two_bank.total_deposits} deposits. ")
#                 if option_choice == 5 and user_two != None:
#                     print(f"There have been {user_two_bank.total_deposits} deposits. ")
#             elif option_choice == 6:
#                 print("Thank you for using BC bank.")
#                 return False
#                 break
#             else:
#                 print("Pleace choose a number from 1-6.")


#     def bank_creation(name):
#         balance = float(input(f"{name.name.title()}, how much money do you have? "))
#         return balance
    
#     while True:
#         print("Welcome to BC Bank")
#         name = input("Enter your name...")
#         age = int(input("Enter your age..."))
#         user_one = User (name, age)
#         user_two = None
#         new_user = input("Would you like to register a new person? Type 'no' to create your bank")
#         if new_user.lower() == 'yes':
#             name = input("Enter the second person's name: ")
#             age = int(input("Enter the second person's age: "))
#             user_two = User(name, age)
#             print("Thank you for registering 2 people. Please create your bank accounts.")
#             user_one_balance = bank_creation(user_one.name)
#             user_two_balance = bank_creation(user_two.name)
#             user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
#             user_two_bank = Bank(user_two.name, user_two.age, user_two_balance)
#             flag = options(user_two)
#             if flag == False:
#                 break
#         else: 
#             user_one_balance = bank_creation(user_one.name)
#             user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
#             flag = options(user_two)
#             if flag == False:
#                 break
           

#3

# class Xodim:
#     def __init__(self, soat, maosh, ism, oy):
#         self.__soat = soat
#         self.__maosh = maosh
#         self.__ism = ism
#         self.__oy = oy 

#     def get_soat(self):
#         return self.__soat

#     def get_maosh(self):
#         return self.__maosh

#     def get_ism(self):
#         return self.__ism

#     def get_oy(self):
#         return self.__oy
        
        
# class calculate:
#     def __init__(self, soat, maosh):
#         self.soat = soat 
#         self.maosh = maosh
#         self.javob = self.soat * self.maosh


# class Manager(calculate):
#     def __init__(self, soat, maosh, ism, oy):
#         super().__init__(soat, maosh)
#         self.ism = ism
#         self.oy = oy

#     def get_maosh(self):
#         return f"{self.ism}, Yillik Maoshi: ${self.javob * (self.oy * 8)}"


# ali = Manager(6, 60, "KADIROv", 4)
# print(ali.get_maosh())


#4

# class Kutubxona:
#     def __init__(self, kitob, muallif) -> None:
#         self.__kitob = kitob
#         self.__muallif = muallif

#     def get_kitobNomi(self):
#         return self.__kitob
    
#     def get_muallif(self):
#         return self.__muallif
    

# class Kitob1(Kutubxona):
#     def __init__(self, kitob, muallif, isbn) -> None:
#         super().__init__(kitob, muallif)
#         self.__isbn = isbn

#     def get_isbn(self):
#         return self.__isbn
    
# class Kitob2(Kutubxona):
#     def __init__(self, kitob, muallif, director) -> None:
#         super().__init__(kitob, muallif)
#         self.__director = director

#     def get_director(self):
#         return self.__director
    
# b1 = Kitob1("DUNYONING ISHLARI", "O'TKIR HOSHIMOV", 6545489849849)
# B2 = Kitob2("HAMLET", "William Shakespeare", "	Shakespearean tragedy")

#5

# class Animal:
#     def __init__(self, nomi, turi, vazni, laqabi, yashash_umri, yemish) -> None:
#         self._nomi = nomi
#         self._turi = turi
#         self._vazni = vazni
#         self._laqabi = laqabi
#         self._yashash_umri = yashash_umri
#         self._yemish = yemish

#     def ov_qilish(self):
#         print("gala bo'lib")
#         print("yolg'iz")
#         print("o'txo'r")
# class Delfin(Animal):
#     def __init__(self, nomi, turi, vazni, laqabi, yashash_umri, yemish) -> None:
#         super().__init__(nomi, turi, vazni, laqabi, yashash_umri, yemish)

#     def ov_qilish(self):
#         print("gala bo'lib")
#         print("yolg'iz")
#         print("o'txo'r")

#     def ovoz(self): 
#         print("Delfinlar ovozi ")

# class Akula(Animal):
#     def __init__(self, nomi, turi, vazni, laqabi, yashash_umri, yemish) -> None:
#         super().__init__(nomi, turi, vazni, laqabi, yashash_umri, yemish)
#     def ov_qilish(self):
#         print("Gala bo'lib baliqlarga hujum qiladi")

# Meg = Akula(nomi="O'lim", turi="baliqsimon", vazni=300, laqabi="shark", yashash_umri=70, yemish="go'sht")
# KUKU = Delfin(nomi="kuku", vazni=80, turi="sutemizuvchi", laqabi="QOPLON",yashash_umri=40, yemish="baliq")
# Meg.ov_qilish()
# KUKU.ovoz()

#10

# class Airline:
#     def __init__(self, nom, aeroport_soni, samolyot_soni):
#         self.nom = nom
#         self.aeroport_soni = aeroport_soni
#         self.samolyot_soni = samolyot_soni


# class Flight:
#     def __init__(self, nom, sigim, yonalish, u_vaqt, q_vaqt, airl):
#         self.q_vaqt = q_vaqt
#         self.u_vaqt = u_vaqt
#         self.yonalish = yonalish
#         self.sigim = sigim
#         self.nom = nom
#         self.airl = airl
#         self.seats = []
#         for i in range(0, sigim):
#             self.seats.append(i)

# class Passenger:
#     def __init__(self, fish, yosh, passport, address):
#         self.__fish = fish
#         self.__yosh = yosh
#         self.__passport = passport
#         self.__address = address

#     def get_fish(self):
#         return self.__fish

#     def get_yosh(self):
#         return self.__yosh

#     def get_passport(self):
#         return self.__passport

# class Booking:
#     def __init__(self, passengers, flight, zakaz_vaqti):
#         self.passengers = passengers
#         self.flight = flight
#         self.zakaz_vaqti = zakaz_vaqti
#         self.price = 250*len(passengers)

# a = Airline("O'zbekiston Havo Yo'llari MCHJ", 8, 95)
# b = Flight("3445A", 200, "Toshkent - NewYork", "08:00", "21:05", a)
# c = Flight("3115B", 320, "Toshkent - Jidda", "11:20", "15:30", a)
# d = Flight("9406A", 300, "Farg'ona - Riyod", "08:00", "21:05", a)

# aa = Passenger("Abduvali Jonbekov", 35, "AA1109080", "Andijon")
# ab = Passenger("Abdushukur Jonbekov", 40, "AA1009180", "Andijon")
# ac = Passenger("Xosiyatxon Jonbekova", 31, "BA1820131", "Andijon")
# ad = Passenger("Hadichaxon Jonbekova", 35, "AB1109170", "Andijon")
# ae = Passenger("Hadichaxon Jonbekova", 35, "AB1109170", "Andijon")

# bb = Booking((aa, ab, ac, ad, ae), c, "20:08")


#6


# class Vehicle:
#     def __init__(self, speed, passenger_capacity):
#         self.__speed = speed
#         self.__passenger_capacity = passenger_capacity

#     def get_speed(self):
#         return self.__speed

#     def get_passenger_capacity(self):
#         return self.__passenger_capacity

#     def accelerate(self):
#         self.__speed += 50

#     def brake(self):
#         if self.__speed >= 10:
#             self.__speed -= 10


# class Car(Vehicle):
#     def __init__(self, speed, passenger_capacity, brand):
#         super().__init__(speed, passenger_capacity)
#         self.__brand = brand

#     def get_brand(self):
#         return self.__brand


# class Bicycle(Vehicle):
#     def __init__(self, speed, passenger_capacity, type):
#         super().__init__(speed, passenger_capacity)
#         self.__type = type

#     def get_type(self):
#         return self.__type


# class Truck(Vehicle):
#     def __init__(self, speed, passenger_capacity, cargo_capacity):
#         super().__init__(speed, passenger_capacity)
#         self.__cargo_capacity = cargo_capacity

#     def get_cargo_capacity(self):
#         return self.__cargo_capacity


# car1 = Car(0, 5, "MAZDA")
# car1.accelerate()
# car1.brake()

# bicycle1 = Bicycle(0, 1, "Aist")
# print(bicycle1.get_type())
# print(bicycle1.get_speed())
# bicycle1.accelerate()
# print(bicycle1.get_speed())
# bicycle1.brake()
# print(bicycle1.get_speed())

# truck1 = Truck(0, 2, "MAN")
# truck1.brake()

#7

# class Mahsulot:
#     def __init__(self, nomi, narxi, maxsulot_soni) -> None:
#         self.__nomi = nomi
#         self.__narxi = narxi
#         self.__maxsulot_soni = maxsulot_soni

#     def get_nom(self):
#         return self.__nomi
#     def get_narxi(self):
#         return self.__narxi
#     def get__maxsulot_soni(self):
#         return self.__maxsulot_soni
    
#     def xisob(self):
#         self_sum = self.__narxi * self.__maxsulot_soni
#         return self_sum
    
# class Un(Mahsulot):
#     def __init__(self, nomi, narxi, maxsulot_soni) -> None:
#         super().__init__(nomi, narxi, maxsulot_soni)
#     def xisob(self):
#         return super().xisob()
    
# TURON = Un(narxi=250000, maxsulot_soni=5, nomi="turon")
# print(TURON.xisob())

#8

# class University:
#     def __init__(self, name):
#         self.__name = name
#         self.__departments = []

#     def get_name(self):
#         return self.__name

#     def add_department(self, department):
#         self.__departments.append(department)

#     def get_departments(self):
#         return self.__departments

# class Department:
#     def __init__(self, name):
#         self.__name = name
#         self.__professors = []
#         self.__students = []

#     def get_name(self):
#         return self.__name

#     def add_professor(self, professor):
#         self.__professors.append(professor)

#     def get_professors(self):
#         return self.__professors

#     def add_student(self, student):
#         self.__students.append(student)

#     def get_students(self):
#         return self.__students


# class Professor:
#     def __init__(self, name, department):
#         self.__name = name
#         self.__department = department

#     def get_name(self):
#         return self.__name

#     def get_department(self):
#         return self.__department


# class Student:
#     def __init__(self, name, department):
#         self.__name = name
#         self.__department = department
#         self.__courses = []
#         self.__grades = {}
#         self.__research_projects = []

#     def get_name(self):
#         return self.__name

#     def get_department(self):
#         return self.__department

#     def add_course(self, course):
#         self.__courses.append(course)

#     def get_courses(self):
#         return self.__courses

#     def assign_grade(self, course, grade):
#         self.__grades[course] = grade

#     def get_grades(self):
#         return self.__grades

#     def add_research_project(self, project):
#         self.__research_projects.append(project)

#     def get_research_projects(self):
#         return self.__research_projects


# university = University("CAMBRIDGE")

# department1 = Department("Computer Science")
# department2 = Department("Mathematics")

# university.add_department(department1)
# university.add_department(department2)

# professor1 = Professor("John Smith", department1)
# professor2 = Professor("Jane Doe", department2)

# department1.add_professor(professor1)
# department2.add_professor(professor2)

# student1 = Student("Alice", department1)
# student2 = Student("Bob", department2)

# department1.add_student(student1)
# department2.add_student(student2)

# student1.add_course("Introduction to Programming")
# student1.add_course("Data Structures")
# student2.add_course("Calculus")
# student2.add_course("Linear Algebra")

# student1.assign_grade("Introduction to Programming", "A")
# student1.assign_grade("Data Structures", "B")
# student2.assign_grade("Calculus", "A-")
# student2.assign_grade("Linear Algebra", "B+")

# student1.add_research_project("Machine Learning")
# student2.add_research_project("Number Theory")

# print(university.get_name())

# departments = university.get_departments()
# for department in departments:
#     print(department.get_name())

#     professors = department.get_professors()
#     for professor in professors:
#         print(professor.get_name())

#     students = department.get_students()
#     for student in students:
#         print(student.get_name())
#         print(student.get_courses())
#         print(student.get_grades())
#         print(student.get_research_projects())



#9



# class User:
#     def __init__(self, name, email, password):
#         self._name = name
#         self.email = email
#         self.password = password
#     def __repr__(self) -> str:
#         return f"NAME : {self._name}, Email: {self.email}"


# class Customer(User):
#     def __init__(self, name, email, password, product_num, price):
#         super().__init__(name, email, password)
#         self.product_num = product_num
#         self._price = price
#         self.total = price * product_num
    
#     def show_total(self):
#         print(f"Your shopping cart: {self.total}sum")
#         return self.total
        

# Ahmad = Customer(name="Ahmad", email="ahmad_qosimov@gmail.com", password="sherqozi_uzb985", price=80000, product_num=10)
# Ahmad.show_total()




#11

# class MORTAL_KOMBAT:
#     def __init__(self, name, xp, first_show, strong_side, weak_side) -> None:
#         self._name = name
#         self._xp = xp
#         self._first_show = first_show
#         self._weak_side = weak_side
#         self._strong_side =strong_side

#     def Block(self):
#         print("L2, R2")

#     def X_ray(self):
#         print("L2 R2 + X")

#     def Hand(self):
#         print(" triangle   rectangle ")
    
#     def Leg(self):
#         print(" O  and X")

#     def __repr__(self) -> str:
#         print(f"""Name: {self._name}\nHalth: {self._xp}\nWeak side: {self._weak_side}s
# The first appearance of the character: {self._first_show} \nThe hero's strength: {self._strong_side}""")

# class Hero(MORTAL_KOMBAT):
#     def __init__(self, name, xp, first_show, strong_side, weak_side) -> None:
#         super().__init__(name, xp, first_show, strong_side, weak_side)
    
# Scorpion = Hero(name="ханзо хасаши", xp=1000, strong_side="FIRE, Chain, Sword, Teleport", weak_side="None", first_show="MK1 - 1995")
# Scorpion.__repr__()
# SubZero = Hero(name="BI-HAN", xp=1000, strong_side="ice, cold, freezing", first_show="MK1 In 1995-year", weak_side="No teleport and almost flawless") 
# SubZero.X_ray()
# SubZero.__repr__()


