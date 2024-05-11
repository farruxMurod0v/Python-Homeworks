class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')

import random

# Random 1000 ta element qo'shish
root = None
for _ in range(1000):
    root = insert(root, random.randint(1, 10000))


print("Preorder Traversal:")
preorder_traversal(root)
print("\n")

print("Postorder Traversal:")
postorder_traversal(root)
print("\n")
