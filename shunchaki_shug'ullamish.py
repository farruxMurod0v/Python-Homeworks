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
     

# import os
# path = "C: \\Users\\Cacow\\Detskop\\folder"
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is  a file")
#     elif os.path.isdir(path):
#         print("That is a directory! ")
#     else:
#         print("That location doesn't exists! ")

# try:
#     with open('amaliyot.py') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found : )")

# with open('1_dars.py') as file:
#     print(file.read())
# print(file.closed)

# text = "yomayooo"
# with open(r"c:\\Users\\HP\\payton darsslari\\1_dars.py", 'w') as file:
#     file.write(text)
#file.closed('1_dars.py')

# import time 
# bomb_time = int (input("Portlatish vaqtini kiriting: "))
# for m in reversed(range(0, bomb_time)):
#     print(m)
#     time.sleep(1)
# print("BOOOOM!!")

# import time
# my_time = int (input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int (x/60) % 60
#     hours = int (x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")


# shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input ("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else :
#         price =  float (input (f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR cart -----")

# for food in foods:
#     print(food)

# for price in prices:
#     total += price

# print(f"Your total is: ${total}")

#   QUIZ GAME

# questions = ("How many elements are in the periodic table?",
#              "Which animal lays the largest eggs?",
#              "What is the most abundant gas in Earth's atmosphere?",
#              "How many bones are in the human body?",
#              "Which planet in the solar system is the hottest?",)

# options =(("A. 116", "B. 117", "C. 118", "D. 119"),
#           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#           ("A. 206", "B. 207", "C. 208", "D. 209"),
#           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")
# geusses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("-------")
#     print(question)
#     for option in options[question_num]:
#         print(option)

#     guess = input("Enter (A,B,C,D:)").upper()
#     geusses.append(guess)
#     if guess == answers[question_num]:
#         score +=1
#         print("Correct!")
#     else:
#         print("Incorrect!")
#         print(f"{answers[question_num]} is the correct answer")    
#     question_num +=1

# print("----------")
# print("     RESULT      ")
# print("----------")

# print("answer:", end="")
# for answer in answers:
#     print(answer, end="")
# print()


# print("guesses: ", end="")
# for guess in geusses:
#     print(guess, end="")
# print()

# score = int (score /len (questions)*100)
# print(f"Your score is: {score} %")
    
    # tosh qaychi qog'oz

# import random

# options  = ("rock", "paper", "scissors")
# player = None
# computer = random.choice (options)

# while player not in options:
#     player(input ("Enter a choice (rock. paper, scissors): "))
#     choice = input("Enter a choice (rock, paper, scissors): ")
# player(choice)
# print(f"player: {player}")
# print(f"computer: {computer}")

# if computer == player:
#     print("It's a tie!")
# elif player == "rock" and computer == "scissors":
#     print("You win")
# elif player == "paper" and computer == "rock":
#     print("you win")
# elif player == "scissors" and computer == "paper":
#     print("You win")
# else :
#     print("You lose")


# import random

# options = ("rock", "paper", "scissors")
# running = True

# while running:
#     player = None
#     computer = random.choice(options)
#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False

# print("Thanks for playing!")


# ● ┌ ─ ┐ │ └ ┘

# import random
# # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2528")
# "┌──────────┐"
# "│          │ "
# "│          │"
# "│          │"
# "└──────────┘"

# dice_art ={
#     1: ("┌─────────┐", 
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐", 
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐", 
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐", 
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐", 
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐", 
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘"),
# }
# total = 0
# dice = []
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range (5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"Total: {total}")

