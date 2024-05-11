# shaharlar = {"Toshkent", "Samarqand", "Buxoro", "Andijon", "Xiva"}
# input_shahar = input("Shahar nomini kiriting: ")
# if input_shahar in shaharlar:
#     shaharlar.remove(input_shahar)
#     print("Setdan", input_shahar, "o'chirildi")
# print("qolgan shaharlar :", shaharlar)












# f
# people = ("Qodir", 99 , 99, "male")
# print(people.count(99))
# print(people.index(99))
# for m in people :
#     print(m)




# print (round(abs(float(input("Enter a whole positive number: ")))))

# name = "MAvlon"

# def display_name():
#     print (name)
# display_name()





# def add(*sonlar):
#     sum = 0
#     for i in sonlar:
#         sum += i
#     return sum
# print(add(98,79,79,87,979,79,95,4949,79,87,87,45454458798,78798))


# str format
# animal = "xo'roz"
# item= "joja"
# print("The "animal + "jumped over the " + item)
# positianal argument 
# print ("The {item} jumped over the {animal}". format (item = "joja" , animal= "xo'roz"))
# text ="The {} junped over the {}"
# print(text.format(animal, item))
# name = "boss"
# print("Hello, my name is {}". format(name))
# print("Hello, my name is {:10}. Nice to meet you ". format(name))
# print("Hello, my name is {:>10}. Nice to meet you ". format(name))
# print("Hello, my name is {:<10}. Nice to meet you ". format(name))
# print("Hello, my name is {:^10}. Nice to meet you ". format(name))

# number = 1000
# print("The number pi is {:.1f}". format(number))
# print("The number  is {:},". format(number))
# print("The number  is {:b}". format(number))
# print("The number  is {:o}". format(number))
# print("The number  is {:X}". format(number))
# print("The number  is {:E}". format(number))

# import random
# x = random.randint(1,600)

# oyn=["tosh", "qaychi", "qog'oz"]
# z = random.choices(oyn)
# print(z)

# cards = [1,2,3,4,5,6,7,8,9,"j", "k", "q", "a"]
# k = random.shuffle(cards)
# print(cards)

# istisnolar 
# try:
#     numerator = int (input ("Enter a number to divide: "))
#     denominator  = int (input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError:
#     print("You can't divide by zero! ideot! ")
# except ValueError:
#     print("Enter only numbers plz")
# except Exception:
#     print("Something went wrong!! )")
# else:
#     print(result)
# finally:
#     print("The will always execute")
     

import os
path = "C: \\Users\\Cacow\\Detskop\\folder"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is  a file")
    elif os.path.isdir(path):
        print("That is a directory! ")
    else:
        print("That location doesn't exists! ")
