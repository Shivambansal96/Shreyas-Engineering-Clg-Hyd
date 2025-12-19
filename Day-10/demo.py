from collections import deque

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         newNode = Node(data)

#         if self.root is None:
#             self.root = newNode
#             return
        
#         q = deque([self.root])

#         while q:
#             temp = q.popleft()

#             if temp.left is None:
#                 temp.left = newNode
#                 return
            
#             else:
#                 q.append(temp.left)

#             if temp.right is None:
#                 temp.right = newNode
#                 return
            
#             else:
#                 q.append(temp.right)

#     def preOrder(self, root):

#         if root is None:
#             return
        
#         print(root.data, end=" -> ")
#         self.preOrder(root.left)
#         self.preOrder(root.right)

#     def levelOrderTraversal(self, root):
#         if root is None:
#             return
        
#         q = deque([root])

#         while q:
#             var = len(q)
            
#             for i in range(var):
#                 temp = q.popleft()

#                 print(temp.data, end=" ")

#                 if temp.left:
#                     q.append(temp.left)

#                 if temp.right:
#                     q.append(temp.right)
#             print()



# bt = Tree()

# bt.insert(5)
# bt.insert(6)
# bt.insert(7)
# bt.insert(8)
# bt.insert(9)
# bt.insert(10)
# bt.insert(11)
# bt.insert(1186)
# bt.insert(1187)

# bt.levelOrderTraversal(bt.root)
# # print(None)



# # # Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, root, data):
        if root is None:
            return self.createNode(data)
        
        if data < root.data:
            root.left = self.insert(root.left, data)

        if data > root.data:
            root.right = self.insert(root.right, data)

        return root
    
    def searchingNod(self, root, key):
        if root is None:
            return 
        
        if root.data == key:
            return "Found" if root else "Not Found"
        
        if root.data < key:
            return self.searchingNod(root.right, key)
        
        if root.data > key:
            return self.searchingNod(root.left, key)

    def levelOrder(self, root):
        if root is None:
            return
        
        q = deque([root])

        while q:
            level = len(q)
            for i in range(level):

                temp = q.popleft()
                
                print(temp.data, end=" ")

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)
            print()

    def smallestValue(self, root):
        if root is None:
            return

        current = root
        while current.left is not None:
            current = current.left

        return current.data

tree = BST()

# root = tree.createNode(5)
root = None
# root = tree.insert(root, 5)
# root = tree.insert(root, 9)
arr = [14, 2, 6, 17, 8, 9, 12, 4, 16]

for i in arr:
    root = tree.insert(root, i)

# tree.levelOrder(root)

# print(f"Smallest Value in BST = {tree.smallestValue(root)}")


print(tree.searchingNod(root, 17))