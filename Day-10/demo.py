# Day 10: Binary Search Trees (BST)

# Topics:
# 1. BST Properties (Left < Root < Right)
# 2. BST Search
# 3. BST Insertion
# 4. BST Deletion (Min/Max, Inorder Predecessor/Successor)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

# Example Usage:
# bst = BST()
# root = None
# keys = [50, 30, 20, 40, 70, 60, 80]
# for key in keys:
#     root = bst.insert(root, key)
# bst.inOrder(root)
