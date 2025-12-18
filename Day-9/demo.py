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

tree = Tree()
root = tree.create(2)
tree.insert(root, 7)
tree.insert(root, 5)
tree.insert(root, 2)
tree.insert(root, 6)

# root.left = tree.create(7)
# root.right = tree.create(5)

# root.left.left = tree.create(2)
# root.left.right = tree.create(6)

print("PreOrder Traversal --> ")
tree.preOrder(root)

print(None)

# print(root.data)


# from collections import deque

# d1 = deque()
# d1.append(76)
# d1.appendleft(987)
# d1.insert(1, 65675)
# print(d1)