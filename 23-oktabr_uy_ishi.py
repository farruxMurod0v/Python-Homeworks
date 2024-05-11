#1


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


#2

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
    
#     def calculate_salary(self):
#         pass

# class Manager(Employee):
#     def __init__(self, name, id, salary):
#         super().__init__(name, id)
#         self.salary = salary
    
#     def calculate_salary(self):
#         return self.salary

# class Engineer(Employee):
#     def __init__(self, name, id, hourly_rate, hours_worked):
#         super().__init__(name, id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
    
#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked

# class Salesperson(Employee):
#     def __init__(self, name, id, base_salary, commission_rate, sales_amount):
#         super().__init__(name, id)
#         self.base_salary = base_salary
#         self.commission_rate = commission_rate
#         self.sales_amount = sales_amount
    
#     def calculate_salary(self):
#         return self.base_salary + (self.commission_rate * self.sales_amount)


# boss = Manager(id=859725, salary=7800, name="Jennie")

# dev = Engineer(id=754895, hourly_rate=3, hours_worked=5, name="Lisa")

# mid = Salesperson(id=989874, base_salary=5, commission_rate=5600, sales_amount=1000000, name="Selena")


#3

# class Music:
#     def __init__(self, music_name, year, singer, music_directions) -> None:
#         self._music_name = music_name
#         self._year = year
#         self._singer = singer
#         self._music_directions = music_directions


# class Artist:
#     def __init__(self, work_name, year, artist, cost) -> None:
#         self.work_name = work_name
#         self.year = year
#         self.artist = artist
#         self.cost = cost


# class Favorites:
#     def __init__(self, name, the_name_of_my_favorite_music) -> None:
#         self.music = []
#         self.work = []
#         self.name = name
#         self.the_name_of_my_favorite_music = the_name_of_my_favorite_music
#     def p_add(self,*music):
#         self.music.append(music)
#         print(music)

# E_M = Music(music_directions="Rap", singer="Eminem", music_name="mockingbird", year=2004)

# M_L = Artist(artist="Leonardo_da_Vinci", work_name="Mona Lisa", cost=505005050, year=1503-1506)

# playlist = Favorites(name="My_musics", the_name_of_my_favorite_music="POP music")
# playlist.p_add("mockingbird", "lovely", "What was I made for?", "Calm Down")


#4



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




#5


# import math

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def area(self):
#         pass
    
#     def perimeter(self):
#         pass
    
#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy
    
#     def resize(self, scale_factor):
#         pass

# class Circle(Shape):
#     def __init__(self, x, y, radius):
#         super().__init__(x, y)
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius**2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius
    
#     def resize(self, scale_factor):
#         self.radius *= scale_factor

# class Rectangle(Shape):
#     def __init__(self, x, y, width, height):
#         super().__init__(x, y)
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
#     def resize(self, scale_factor):
#         self.width *= scale_factor
#         self.height *= scale_factor





#6

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.menu = {}

#     def add_item_to_menu(self, item_name, price):
#         self.menu[item_name] = price

#     def remove_item_from_menu(self, item_name):
#         if item_name in self.menu:
#             del self.menu[item_name]

#     def display_menu(self):
#         print(f"Menu for {self.name}:")
#         for item, price in self.menu.items():
#             print(f"{item}: sum{price}")

# restaurant = Restaurant("QARSILAMA SOMSALAR", "TOSHKENT")

# restaurant.add_item_to_menu("tovuq somsa", 25000)
# restaurant.add_item_to_menu("mol go'shti", 35000)
# restaurant.add_item_to_menu("qo'y go'shti", 30000)

# restaurant.display_menu()
# restaurant.remove_item_from_menu("Salad")
# restaurant.display_menu()


#7



from tkinter import *
from tkinter import ttk

def print():
    tott = float(totText.get())
    top = Toplevel()
    top.geometry("300x300")
    top.config(bg="white")
    l = Label(top, text='---------RECIEPT----------')
    l.pack()
    l.config(bg="white")
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")

    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()

    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()


def show():
    tot = 0
    if (var1.get()):
        price = int(e1.get())
        qty = int(e6.get())
        tot = int(price * qty)
        tempList = [['Coca Cola', e1.get(), e6.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var2.get()):
        price = int(e2.get())
        qty = int(e7.get())
        tot = int(price * qty)
        tempList = [['Bun', e2.get(), e7.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var3.get()):
        price = int(e3.get())
        qty = int(e8.get())
        tot = int(price * qty)
        tempList = [['Chicken Fry', e3.get(), e8.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var4.get()):
        price = int(e4.get())
        qty = int(e9.get())
        tot = int(price * qty)
        tempList = [['Roll', e4.get(), e9.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var5.get()):
        price = int(e5.get())
        qty = int(e10.get())
        tot = int(price * qty)
        tempList = [['Fish Fried Rice', e5.get(), e10.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)


root = Tk()
root.title("Bill Print Inventory System using Python")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText

totText = StringVar()
balText = IntVar()

Label(root, text="Bill Print Inventory System using Python", font="arial 22 bold" ,bg="white").place(x=5, y=10)


var1 = IntVar()
Checkbutton(root, text="Coca Cola", variable=var1).place(x=10, y=50)

var2 = IntVar()
Checkbutton(root, text="Bun", variable=var2).place(x=10, y=80)

var3 = IntVar()
Checkbutton(root, text="Chicken Fry", variable=var3).place(x=10, y=110)

var4 = IntVar()
Checkbutton(root, text="Roll", variable=var4).place(x=10, y=140)

var5 = IntVar()
Checkbutton(root, text=" Fish Fried Rice  ", variable=var5).place(x=10, y=170)
Label(root, text="Total").place(x=600, y=10)

e1 = Entry(root)
e1.place(x=140, y=50)

e2 = Entry(root)
e2.place(x=140, y=80)

e3 = Entry(root)
e3.place(x=140, y=110)

e4 = Entry(root)
e4.place(x=140, y=140)

e5 = Entry(root)
e5.place(x=140, y=170)

e6 = Entry(root)
e6.place(x=300, y=50)

e7 = Entry(root)
e7.place(x=300, y=80)

e8 = Entry(root)
e8.place(x=300, y=110)

e9 = Entry(root)
e9.place(x=300, y=140)

e10 = Entry(root)
e10.place(x=300, y=170)

tot = Label(root, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=650, y=10)

Button(root, text="Add", command=show, height=3, width=13).place(x=10, y=220)

Button(root, text="Print", command=print, height=3, width=13).place(x=850, y=120)
cols = ('item', 'price', 'qty', 'total')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=300)


root.mainloop()




#####


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.stock_level = 0
    
#     def restock(self, quantity):
#         self.stock_level += quantity
    
#     def sell(self, quantity):
#         if self.stock_level >= quantity:
#             self.stock_level -= quantity
#             return True
#         else:
#             return False

# class Order:
#     def __init__(self):
#         self.products = []
    
#     def add_product(self, product, quantity):
#         self.products.append((product, quantity))
    
#     def process_order(self):
#         for product, quantity in self.products:
#             if not product.sell(quantity):
#                 return False
#         return True

# class InventorySystem:
#     def __init__(self):
#         self.products = []
    
#     def add_product(self, name, price):
#         product = Product(name, price)
#         self.products.append(product)
    
#     def restock_product(self, name, quantity):
#         for product in self.products:
#             if product.name == name:
#                 product.restock(quantity)
#                 return True
#         return False
    
#     def create_order(self):
#         order = Order()
#         return order
    
#     def report_stock_levels(self):
#         for product in self.products:
#             print(f"{product.name}: {product.stock_level}")
