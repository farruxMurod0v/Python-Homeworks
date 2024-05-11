



# from abc import ABC, abstractmethod


# class ShipBlueprint(ABC):
#     @abstractmethod
#     def tezlashish(self):
#         pass

#     def yelkanlarni_kotarish(self):
#         pass

#     @abstractmethod
#     def burilish(self):
#         pass

#     @abstractmethod
#     def langar_tashlash(self):
#         pass

#     @abstractmethod
#     def tor_tashlash(self):
#         pass

#     @abstractmethod
#     def danger(self):
#         pass




# class Ship(ShipBlueprint):
#     def tezlashish(self, a=10):
#         if self.__tezlik + a <= self.__max_tezlik:
#             print(f"tezlik {a} ga oshirildi") 

#     def burilish(self, Tomon):
#         if Tomon == "left" :
#             print("Kemani chapga buring")

#         elif Tomon == "right":
#             print("kemani o'ngga buring")

#         else:
#             print("faqat oldinga")

#     def langar_tashlash(self, C):
#         if C == True:
#             print("Langarlar ko'tarilsin")
#         elif C == False:
#             print("Langarlar tushurilsin")

#     def tor_tashlash(self, tor):
#         if tor == "Yes":
#             print("To'r tashlaymiz va baliq tutamiz")
#         elif tor == "No":
#             print("bugun baliq ovi bo'lmaydi havo yomon")
#     def danger(self, d):
#         if d == True:
#             print("xavf yordam")

#         else:
#             print("Tinchlik")

#     def __init__(self, nom, brend, sigim, max_tezlik, narx):
#         self.__nom = nom
#         self.__narx = narx
#         self.__max_tezlik = max_tezlik
#         self.__sigim = sigim
#         self.__brend = brend
#         self.__tezlik = 0
#         self.__langar_pastda = True
#         self.__yeklan = False
#         self.__sos = "SOS SOS SOS YORDAM PLIZ"



# Qora_marvarid = Ship(brend="APL", narx=10000000, sigim=2400, max_tezlik=250, nom="Qora Marvarid")
# Qora_marvarid.burilish(Tomon="left")
# Qora_marvarid.tezlashish(a=50)
# Qora_marvarid.tor_tashlash("Yes")
# Qora_marvarid.danger("No")



#1
from datetime import datetime, date, time
# University system
hozirgi_voqt = datetime.now()
class University:
    def __init__(self, name):
        self.__name = name
        self.__departments = []

    def get_name(self):
        return self.__name

    def add_department(self, department):
        self.__departments.append(department)

    def get_departments(self):
        return self.__departments

class Department:
    def __init__(self, name):
        self.__name = name
        self.__professors = []
        self.__students = []

    def get_name(self):
        return self.__name

    def add_professor(self, professor):
        self.__professors.append(professor)

    def get_professors(self):
        return self.__professors

    def add_student(self, student):
        self.__students.append(student)

    def get_students(self):
        return self.__students


class Professor:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department


class Student:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department
        self.__courses = []
        self.__grades = {}
        self.__research_projects = []

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def add_course(self, course):
        self.__courses.append(course)

    def get_courses(self):
        return self.__courses

    def assign_grade(self, course, grade):
        self.__grades[course] = grade

    def get_grades(self):
        return self.__grades

    def add_research_project(self, project):
        self.__research_projects.append(project)

    def get_research_projects(self):
        return self.__research_projects


university = University("CAMBRIDGE")

department1 = Department("Computer Science")
department2 = Department("Mathematics")

university.add_department(department1)
university.add_department(department2)

professor1 = Professor("John Smith", department1)
professor2 = Professor("Jane Doe", department2)

department1.add_professor(professor1)
department2.add_professor(professor2)

student1 = Student("Alice", department1)
student2 = Student("Bob", department2)

department1.add_student(student1)
department2.add_student(student2)

student1.add_course("Introduction to Programming")
student1.add_course("Data Structures")
student2.add_course("Calculus")
student2.add_course("Linear Algebra")

student1.assign_grade("Introduction to Programming", "A")
student1.assign_grade("Data Structures", "B")
student2.assign_grade("Calculus", "A-")
student2.assign_grade("Linear Algebra", "B+")

student1.add_research_project("Machine Learning")
student2.add_research_project("Number Theory")

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
# tugagan_voqt = datetime.now()
# print(tugagan_voqt - hozirgi_voqt,"kod ishlashiga ketgan vaqt")




#3
# import datetime

# date_string = "April 1, 2015 12:40"
# date_object = datetime.datetime.strptime(date_string, "%B %d, %Y %H:%M")
# print(date_object)



#2

import datetime

#a) 
current_date = datetime.datetime.now()
formatted_date_a = current_date.strftime("%Y, %d-%b")
print("Format a:", formatted_date_a)

#b): 
formatted_date_b = current_date.strftime("%d.%m.%Y")
print("Format b:", formatted_date_b)

#c): 
formatted_date_c = current_date.strftime("%d-%b, %Y-yil")
print("Format c:", formatted_date_c)


#4

print(datetime.weekday(2021, 5, 12))

