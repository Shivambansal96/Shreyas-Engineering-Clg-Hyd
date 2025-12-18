# Bit Manipulation Leftovers
def find_unique(arr):
    """
    Find the unique element in an array where every other element appears twice.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    unique = 0
    for num in arr:
        unique ^= num
    return unique

def decimal_to_binary(n):
    """
    Convert a decimal number to binary without using bin() method.
    """
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

print("--- Bit Manipulation ---")
print(f"Unique element in [2, 3, 5, 4, 5, 3, 4]: {find_unique([2, 3, 5, 4, 5, 3, 4])}")
print(f"Binary of 10: {decimal_to_binary(10)}")
print(f"Binary of 25: {decimal_to_binary(25)}")
print()

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def create(self, data):
        return Node(data)
    
    def insert(self, root, data):
        """
        Level-order insertion using deque
        """
        newNode = Node(data)

        if root is None:
            return newNode
        
        q = deque([root])

        while q:
            temp = q.popleft()

            if temp.left is None:
                temp.left = newNode
                return root
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = newNode
                return root
            else:
                q.append(temp.right)

    def preOrder(self, root):
        if root is None:
            return
        print(root.data, end=" -> ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=" -> ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=" -> ")

    def levelOrder(self, root):
        if root is None:
            return
        q = deque([root])
        while q:
            temp = q.popleft()
            print(temp.data, end=" -> ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

print("--- Binary Tree ---")
tree = Tree()
root = tree.create(2)
tree.insert(root, 7)
tree.insert(root, 5)
tree.insert(root, 2)
tree.insert(root, 6)
tree.insert(root, 9)
tree.insert(root, 5)
tree.insert(root, 11)
tree.insert(root, 4)

print("PreOrder Traversal:")
tree.preOrder(root)
print("None")

print("\nInOrder Traversal:")
tree.inOrder(root)
print("None")

print("\nPostOrder Traversal:")
tree.postOrder(root)
print("None")

print("\nLevelOrder Traversal:")
tree.levelOrder(root)
print("None")
