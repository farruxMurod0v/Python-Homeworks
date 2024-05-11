# # telegram messenger
#
# class Messenger:
#     def __init__(self, user, password):
#         self.user = user
#         self.password = password
#         self.input_message = []
#         self.output_message = []
#         self.status = []
#
#     def send_message(self, other_user, text):
#         # Sending message to other_user
#         self.output_message.append(text)
#         self.status.append('Sent')
#         other_user.input_message.append(text)
#         other_user.status.append('Received')
#
#     def read_message(self):
#         # Reading the messages
#         for i in range(len(self.input_message)):
#             self.status[i] = 'Read'
#
#     def send_file(self, other_user, file_name):
#         # Sending file to other_user
#         self.output_message.append(file_name)
#         self.status.append('Sent')
#         other_user.input_message.append(file_name)
#         other_user.status.append('Received')
#
#     def read_file(self):
#         # Reading the files
#         for i in range(len(self.input_message)):
#             if isinstance(self.input_message[i], str):
#                 self.status[i] = 'Read'
#
#     def delete(self):
#         # Deleting the messages and files
#         self.input_message = []
#         self.output_message = []
#         self.status = []
#
#


# # Creating two objects of the Messenger class
# user1 = Messenger(user='user1_telegram', password='password1')
# user2 = Messenger(user='user2_telegram', password='password2')
#
# # Using the methods of the Messenger class for the two objects
# user1.send_message(user2, text="Hello, how are you?")
# user2.read_message()
# user2.send_file(user1, file_name="tg.txt")
# user1.read_file()
# user1.delete()
# user2.delete()

#
# def add_brackets(input_string):
#     result = ""
#     for i in range(len(input_string)):
#         if i % 2 == 0:
#             result += "(" + input_string[i]
#         else:
#             result += input_string[i] + ")"
#     if len(input_string) % 2 == 0:
#         result = result[:len(result)//2] + "()" + result[len(result)//2:]
#     return result
#
# input_string = input("Enter a string: ")
# print(add_brackets(input_string))


# def add_parentheses(word):
#     parentheses = ""
#     for letter in word:
#         parentheses += "(" + letter + ")"
#     return parentheses
#
# word = input("Enter a word: ")
# if len(word) % 2 == 0:
#     middle_pos = len(word) // 2 - 1
# else:
#     middle_pos = len(word) // 2
#
# parentheses_word = add_parentheses(word[:middle_pos]) + word[middle_pos] + add_parentheses(word[middle_pos+1:])
# print(parentheses_word)


# lst = input("Enter a list of integers separated by spaces: ")
# lst = list(map(int, lst.split()))
#
# pair_count = 0
# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if lst[i] == lst[j]:
#             pair_count += 1
#
# print("Number of pairs of equal elements:", pair_count)



#
#
# with open('input.txt', 'w') as input_file:
#     data = input_file.read()
#
# data = data.replace('\n', '')
# data = list(data)
#
# for i in range(len(data)):
#     if data.count(data[i]) > 1:
#         data[i] = '*'
#
# result = ''.join(data)
#
# with open('output.txt', 'w') as output_file:
#     output_file.write(result)



# bowling
#
# n, k = map(int, input().split())
# l = list("|" * n)
# for _ in range(k):
#     a, b = map(int, input().split())
#     for i in range (a-1, b):
#         l[i] = "*"
# print(*l)

