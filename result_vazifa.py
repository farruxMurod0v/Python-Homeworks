# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

# class TimeTable(Time):
#     def __init__(self, subject, start_time, classroom):
#         self.subject = subject
#         self.start_time = start_time
#         self.classroom = classroom

# lesson1 = TimeTable("Math", Time(9, 0, 0), "Room 11")
# lesson2 = TimeTable("English", Time(10, 30, 0), "Room 12")
# lesson3 = TimeTable("Science", Time(13, 0, 0), "Lab 13")
# lesson4 = TimeTable("History", Time(14, 30, 0), "Room 14")
# lesson5 = TimeTable("Art", Time(16, 0, 0), "Art Studio")

# user_hour = int(input("Soatni kiriting: "))
# user_minute = int(input("Minutni kiriting: "))
# user_second = int(input("Sekunndni kiriting: "))

# user_time = Time(user_hour, user_minute, user_second)

# for lesson in [lesson1, lesson2, lesson3, lesson4, lesson5]:
#     if lesson.start_time.hour == user_time.hour and lesson.start_time.minute == user_time.minute and lesson.start_time.second == user_time.second:
#         print(f"{lesson.subject} fanining dars boshlanishi {user_time.hour}:{user_time.minute}:{user_time.second} da boshlanadi.")

#2

N = int(input("Matritsa o'lchamini kiriting: "))

matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

with open('matrix.txt', 'w') as file:
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')