# # E-commerce Platform:
# # Create a sophisticated e-commerce platform
# # with classes for User, Product, ShoppingCart, and Order.
# # Users can be both customers and sellers.
# # Implement an intricate order processing system,
# # with multiple payment methods and shipping options.
# # Apply encapsulation to secure user
# # and payment information.
# # Demonstrate polymorphism by processing
# # orders from different types of users.


#2


# class Cart:
#     def __init__(self, id, user, sana, holat):
#         self.__id = id
#         self.__user = user
#         self.__sana = sana
#         self.holat = holat
#         self.__narx = 0
#         self.__bonus = 0

#     def get_narx(self):
#         print(f"Narx:{self.__narx}\nBonus:{self.__bonus}")
#         return self.__narx

#     def set_narx(self, a):
#         self.__narx += a-a/20
#         self.__bonus += a/20



# class Order:
#     def __init__(self, product, amount, cart):
#         self.product = product
#         self.amount = amount
#         self.cart = cart
#         self.narx = product._narx * amount
#         cart.set_narx(self.narx)
#         product._user.set_daromad(self.narx)


# class Product:
#     def __init__(self, nom, narx, sana, user):
#         self._nom = nom
#         self._narx = narx
#         self._sana = sana
#         self._user = user


# class Cloth(Product):
#     def __init__(self, nom, narx, sana, user, brend, size, rang):
#         super().__init__(nom, narx, sana, user)
#         self._brend = brend
#         self._size = size
#         self._rang = rang


# class Gadget(Product):
#     def __init__(self, model, narx, sana, user, brend, tur, holat):
#         super().__init__(model, narx, sana, user)
#         self.brend = brend
#         self.tur = tur
#         self.holat = holat

# class User:
#     def __init__(self, fish, email, telefon, yil, jins, manzil):
#         self.__manzil = manzil
#         self.__jins = jins
#         self.__yil = yil
#         self.__telefon = telefon
#         self.__email = email
#         self.__fish = fish
#         self.__daromad = 0


#     def set_daromad(self, a):
#         self.__daromad += a

#     def get_daromad(self):
#         return self.__daromad

#     def get_manzil(self):
#         return self.__manzil

#     def get_jins(self):
#         return self.__jins

#     def get_email(self):
#         return self.__email

#     def get_telefon(self):
#         return self.__telefon

#     def get_fish(self):
#         return self.__fish

#     def get_yil(self):
#         return self.__yil




# u = User("Abduvali Rajabov", "abdushka@sfak.com",
#          "99 999 88 78", 1984, "M",
#          "Qo'qon shahar, Marifat 28")
# u1 = User("Abdushukur Holmatov", "hheehee@sfak.com",
#          "91 988 09 78", 1981, "M",
#          "Andijon shahar, Shaytanat 128")
# u2 = User("Toshtemir Toshov", "stone@sfak.com",
#          "91 008 09 07", 2001, "M",
#          "Toshkent, Toshko'mirchi 101")


# p1 = Cloth("T-shirt 99", 23, "09.09.2023", u2, "Tommy Hilfiger", "L", "white")
# p2 = Cloth("Jacket 101", 320, "09.09.2023", u2, "Tommy Hilfiger", "XL", "black", )
# p3 = Cloth("Trousers ff4", 132, "09.09.2023", u2,  "Fashion", "M", "khaki")
# p4 = Cloth("T-shirt ", 48, "09.09.2023", u2,  "Levi's", "XL", "cyan")
# p5 = Gadget("iPhone 13 pro Max", 1200, "09.09.2022", u2, "Apple", "smartphone", "new")
# p6 = Gadget("Galaxy S23 pro Max", 1100, "08.09.2022", u2, "Samsung", "smartphone", "new")


# c1 = Cart(1, u, "10.10.2023", "pending")
# c2 = Cart(2, u1, "10.11.2023", "pending")


# o1 = Order(p1, 4, c1)
# o2 = Order(p4, 2, c1)
# o3 = Order(p6, 1, c1)
# o4 = Order(p5, 2, c2)
# o5 = Order(p2, 5, c2)

# c1.get_narx()
# c2.get_narx()
# print("Foydalanuvchi daromadi: ", u2.get_daromad())




# 1

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



#3


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






#4

class Player:
    def __init__(self, name, club, height, weight, age, rating)-> None:
                 self._name = name
                 self._club = club
                 self._height = height
                 self._weight = weight
                 self._age = age
                 self._rating = rating


class  Attacking:
        def __init__(self, offensive_awareness, ball_control, dribbling, tight_possession,
                     low_pass, lofted_pass, finishing, header, pleace_kicking, curl) -> None:
                self._offensive_awareness = offensive_awareness
                self._ball_control = ball_control
                self._dribbling = dribbling
                self._tight_possession = tight_possession
                self._low_pass = low_pass
                self._lofted_pass = lofted_pass
                self._finishing =finishing
                self._header = header
                self._pleace_kicking = pleace_kicking
                self._curl = curl


class Defending:
        def __init__(self, D_awareness, D_engagement, tackling, aggression) -> None:
                self._D_awareness = D_awareness
                self._ = D_engagement
                self._tackling = tackling
                self._aggression = aggression


class Athletiscism:
        def __init__(self, speed, acceleration, kicking_power, jump, physical_contact, balance, stamina) -> None:
                self._speed = speed
                self._acceleration = acceleration
                self.kicking_power = kicking_power
                self._jump = jump
                self._physical_contact = physical_contact
                self.balance = balance
                self._stamina = stamina


class Player_skills:
        def Scissors_Feint(self):
            print("Enables players to execute the Scissors Feint at high speed.")

        def Double_Touch(self):
            print("Enables players to quickly execute the Double Touch.")

        def Flip_Flap(self):
            print("Enables players to execute the Flip Flap.")

        def Marseille_Turn(self):
            print("Enables lavers to execute the Marseille Turn.")

        def Sombrero(self):
            print("Enables players to execute the Boomerang Trap and the Sombrero Turn.")

        def Chop_Turn(self):
            print("Enables plavers to quickly execute the Chop Turn.")

        def Cut_Behind_Turn(self):
            print("Enables players to execute the Cut Behind.")

        def Scotch_Move(self):
            print("Enables players to execute the Scotch Move.")

        def Sole_Control(self):
            print("Enables step on ball control to execute feints and turns.")

        def Heading(self):
            print("Improves the accuracy of headers as well as the frequency of downward headers.")
        
        def Long_Range_Curler(self):
            print("Enables players to hit curling shots with great accuracy from a distance.")

        def Chip_Shot_Control(self):
            print("Enables accurate chip shots.")

        def Enables_accurate_chip_shots(self):
            print("The player becomes more accurate at long-range shots.")

        def  Knuckle_Shot(self):
            print("Enables players to hit knuckle shots with greater ease, also applies to Free Kicks.")

        def Dipping_Shot(self):
            print("Enables top spin shots that bounce erratically in front of the goalkeeper.")
       
        def Rising_Shot(self):
            print("Enables shots that begin with a low trajectory that rise sharply.")

        def Acrobatic_Finishing(self):
            print("Enables players to find a finish even from awkward positions or when off balance.")

        def Heel_Trick(self):
            print("Enables players to pass and shoot using the heel, even from awkward positions or when offbalance.")

        def First_time_Shot(self):
            print("Improves technique and precision when taking first-time shots.")

        def One_touch_Pass(self):
            print("Improves technique and precision when playing one-touch passes.")

        def Through_Passing(self):
            print("Increases the accuracy of the plaver's through balls")

        def Weighted_Pass(self):
            print("Enables players to apply back-spin when playing lofted passes and through balls improvingaccuracv")

        def Pinpoint_Crossing(self):
            print("Enables players to curl in crosses with great accuracy.")

        def Outside_Curler(self):
            print("Enables players to shoot and pass using the outside of the boot even at long distances.")

        def Rabona(self):
            print("Enables players to execute a Rabona and means they can pass or shoot when the opposition is not expecting it.")

        def No_Look_Pass(self):
            print("Enables passes that misdirect opponents.")

        def Low_Lofted_Pass(self):
            print("Enables players to hit a long accurate Lofted Pass with a low trajectory when appropriate.")

        def GK_Low_Punt(self):
            print("Enables goalkeepers to take long accurate punt kicks with a low trajectory.")

        def GK_High_Punt(self):
            print("Enables goalkeepers to take long, high punt kicks that end up deep in opposition territory.")

        def Long_Throw(self):
            print("Improves the range of long throws.")

        def GK_Long_Throw(self):
            print("Improves the range on throws by the goalkeeper")

        def Penalty_Specialist(self):
            print("Enables higher accuracy penalty kicks.")

        def GK_Penalty_Saver(self):
            print("Enables better goalkeeping reactions against penalty kicks.")

        def Gamesmanship (self):
            print("Enables players to win free kicks when on the ball.")

        def Man_Marking(self):
            print("Enables the player to stick to and persistently chase down an opponent.")

        def Track_Back(self):
            print("""The player aggressively pressures the opposition player who is on the ball all the way from
the frontlines.""")

        def Interception(self):
            print("Enables better interception skills.")

        def Blocker(self):
            print("Improves the player's chances to block passes and shots.")

        def Aerial_Superiority(self):
            print("Improves the player's chances to win aerial balls.")

        def Sliding_Tackle(self):
            print("Improves the player's chances to gain ball control through a sliding tackle.")

        def Acrobatic_Clearance(self):
            print("Enables players to clear the ball using their feet, even from awkward positions.")

        def Captaincy(self):
            print("Become the team's inspiration on the pitch, reducing the effects of fatigue for all the team.")
        
        def Super_sub(self):
            print("Improves players abilities when introduced in the second half of the game.")

        def Fighting_Spirit(self):
            print("Enables players to perform better under pressure and fatigue, as well as adversity.")

class Goalkeeper(Player_skills):
    def Captaincy(self):
         return super().Captaincy()
    
    def Fighting_Spirit(self):
         return super().Fighting_Spirit()
    
    def GK_High_Punt(self):
         return super().GK_High_Punt()
    def GK_Long_Throw(self):
         return super().GK_Long_Throw()
    
    def GK_Penalty_Saver(self):
         return super().GK_Penalty_Saver()


class Offensive_Wingback(Player_skills):
    def Acrobatic_Finishing(self):
         return super().Acrobatic_Finishing()
    
    def First_time_Shot(self):
         return super().First_time_Shot()
    
    def Knuckle_Shot(self):
         return super().Knuckle_Shot()
    
    def Long_Range_Curler(self):
         return super().Long_Range_Curler()
    
    def Long_Throw(self):
         return super().Long_Throw()
    
    def Low_Lofted_Pass(self):
         return super().Low_Lofted_Pass()
    
    def Pinpoint_Crossing(self):
         return super().Pinpoint_Crossing()
    
    def Rising_Shot(self):
         return super().Rising_Shot()
    

class Ofensive_WingbackR(Offensive_Wingback, Player_skills):
    def Acrobatic_Clearance(self):
         return super().Acrobatic_Clearance()
    
    def Fighting_Spirit(self):
         return super().Fighting_Spirit()
    
    def Flip_Flap(self):
         return super().Flip_Flap()
    
    def Interception(self):
         return super().Interception()
    
    def Man_Marking(self):
         return super().Man_Marking()
    
    def Pinpoint_Crossing(self):
         return super().Pinpoint_Crossing()
    
    def Rabona(self):
         return super().Rabona()

    def Rising_Shot(self):
         return super().Rising_Shot()

    def Sombrero(self):
         return super().Sombrero()
    
    def Weighted_Pass(self):
         return super().Weighted_Pass()
    


class Destroyer_sv(Player_skills):
    def Captaincy(self):
         return super().Captaincy()
    
    def Heel_Trick(self):
         return super().Heel_Trick()
    
    def Interception(self):
         return super().Interception()
    
    def Man_Marking(self):
         return super().Man_Marking()
    
    def Pinpoint_Crossing(self):
         return super().Pinpoint_Crossing()
    
    def Weighted_Pass(self):
         return super().Weighted_Pass()
    
    def Sliding_Tackle(self):
         return super().Sliding_Tackle()
    
    def Aerial_Superiority(self):
         return super().Aerial_Superiority()
    
    def Blocker(self):
         return super().Blocker()
    


class SMF_AMF_DMF (Player_skills):
     def Captaincy(self):
          return super().Captaincy()
     
     def Fighting_Spirit(self):
          return super().Fighting_Spirit()
     
     def Long_Range_Curler(self):
          return super().Long_Range_Curler()
     
     def Weighted_Pass(self):
          return super().Weighted_Pass()
     
     def One_touch_Pass(self):
          return super().One_touch_Pass()
     
     def Low_Lofted_Pass(self):
          return super().Low_Lofted_Pass()
     
     def Penalty_Specialist(self):
          return super().Penalty_Specialist()
     
     def Outside_Curler(self):
          return super().Outside_Curler()
     
    
class SF(Player_skills):
    
    def Captaincy(self):
         return super().Captaincy()
    
    def  Chip_Shot_Control(self):
         return super().Chip_Shot_Control()
    
    def Dipping_Shot(self):
         return super().Dipping_Shot()
    
    def Double_Touch(self):
         return super().Double_Touch()
    
    def First_time_Shot(self):
         return super().First_time_Shot()
    
    def Long_Range_Curler(self):
         return super().Long_Range_Curler()
    
    def One_touch_Pass(self):
         return super().One_touch_Pass()
    
    def Penalty_Specialist(self):
         return super().Penalty_Specialist()
    
    def Through_Passing(self):
         return super().Through_Passing()
    


GK = Player(name="O.KAHN", club="FC Bayern Munchen", age=31, height=188, weight=91, rating=102)
GK = Goalkeeper()


Lb = Player(name="Roberto Carlos", club="Real Madrid", weight=73, height=168, age=24, rating=101)
lb = Ofensive_WingbackR()


SB = Player(name="P. Maldini", club="Milan", age=26, height=186, weight=85, rating=101)
SB = Destroyer_sv()


SB2 = Player(name="F.Beckenbauer", club="FC Bayern Munchen", age=29, weight=77, height=181, rating=100)
SB2 = Destroyer_sv()


RB = Player(name="Cafu", club="Milan", age=34, height=176, weight=75, rating=99)
RB = Ofensive_WingbackR()


DMF = Player(name="J.Kimmich", club="FC Bayern Munchen", age=28, height=177, weight=75, rating=100)
DMF = SMF_AMF_DMF()


AMF = Player(name="Ronaldinho.G", club="Barcelona", age=25, height=182, weight=80, rating=102)
AMF = SMF_AMF_DMF()


SMF = Player(name="D.Beckham", club="Manchester United FC", age=24, height=183, weight=76, rating=102)
SMF = SMF_AMF_DMF()


LN = Player(name="C.Ronaldo", club="Al-Nassr", age=38, height=187, weight=84, rating=96)
LN = SF()


S_F = Player(name="M.OWen", club="Liverpool", age=21, height=173, weight=70, rating=100)
S_F = SF()


RWF = Player(name="L.Messi", club="Miami", age=36, height=170, weight=72, rating=103)
RWF = SF()



from abc import ABC, abstractmethod


class ShipBlueprint(ABC):
    @abstractmethod
    def tezlashish(self):
        pass

    def yelkanlarni_kotarish(self):
        pass

    @abstractmethod
    def burilish(self):
        pass

    @abstractmethod
    def langar_tashlash(self):
        pass

    @abstractmethod
    def tor_tashlash(self):
        pass

    @abstractmethod
    def danger(self):
        pass




class Ship(ShipBlueprint):
    def tezlashish(self, a=10):
        if self.__tezlik + a <= self.__max_tezlik:
            print(f"tezlik {a} ga oshirildi") 

    def burilish(self, Tomon):
        if Tomon == "left" :
            print("Kemani chapga buring")

        elif Tomon == "right":
            print("kemani o'ngga buring")

        else:
            print("faqat oldinga")

    def langar_tashlash(self, C):
        if C == True:
            print("Langarlar ko'tarilsin")
        elif C == False:
            print("Langarlar tushurilsin")

    def tor_tashlash(self, tor):
        if tor == "Yes":
            print("To'r tashlaymiz va baliq tutamiz")
        elif tor == "No":
            print("bugun baliq ovi bo'lmaydi havo yomon")
    def danger(self, d):
        if d == True:
            print("xavf yordam")

        else:
            print("Tinchlik")

    def __init__(self, nom, brend, sigim, max_tezlik, narx):
        self.__nom = nom
        self.__narx = narx
        self.__max_tezlik = max_tezlik
        self.__sigim = sigim
        self.__brend = brend
        self.__tezlik = 0
        self.__langar_pastda = True
        self.__yeklan = False
        self.__sos = "SOS SOS SOS YORDAM PLIZ"



Qora_marvarid = Ship(brend="APL", narx=10000000, sigim=2400, max_tezlik=250, nom="Qora Marvarid")
Qora_marvarid.burilish(Tomon="left")
Qora_marvarid.tezlashish(a=50)
Qora_marvarid.tor_tashlash("Yes")
Qora_marvarid.danger("No")






