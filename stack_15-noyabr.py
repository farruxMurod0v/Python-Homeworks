# class Stack:
#     def __init__(self, a=20):
#         self.stack = []
#         self.size = a
#         self.top = -1
#
#     def push(self, a):
#         if self.isFull():
#             return
#         else:
#             self.stack.append(a)
#
#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False
#
#     def isFull(self):
#         if self.top + 1 == self.size:
#             return True
#         else:
#             return False
#
#

#
# class Stack:
#     def __init__(self, a=10):
#         self.stack = []
#         self.size = a
#         self.top = 0
#
#
#     def isFull(self):
#         if self.top == self.size:
#             return True
#         return False
#
#
#     def isEmpty(self):
#         if self.top == 0:
#             return True
#         return False
#
#     def push(self, a):
#         if self.isFull():
#             print("Stack Overflow!!!!!")
#             return
#         self.stack.append(a)
#         print(f"{a} qo'shildi")
#         self.top += 1
#
#
#     def pop(self):
#         if self.isEmpty():
#             print("Stack Underflow!!!")
#             return
#         self.top -= 1
#         print(f"{self.stack[-1]} o'chirildi!")
#         self.stack.pop()
#
# #
#     def top(self):
#         if self.isEmpty():
#             print("Stack is Empty!!!!!")
#             return
#         return self.stack[-1]
#
#
# s = Stack(5)
# s.push(25)
# s.push(30)
# s.push(1)
# s.pop()
# s.pop()
# s.pop()
# s.pop()
#






class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

    def size(self):
        return len(self.items)

# Example usage:
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Peek at the front element without removing it
front_element = my_queue.peek()
print("Front element:", front_element)

# The queue remains unchanged
print("Queue size after peek:", my_queue.size())







