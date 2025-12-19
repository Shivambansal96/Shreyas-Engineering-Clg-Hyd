class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, root, data):
        if root is None:
            return self.createNode(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root
    
    def deleteNode(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.data:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # Node with only one child or no child
                
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the in order successor (smallest in the right subtree)
            # temp = self.minValueNode(root.left) # Doesn't matter what you choose for two children
            temp = self.minValueNode(root.right)


            # Copy the in order successor's content to this node
            root.data = temp.data

            # Delete the In order successor
            root.right = self.deleteNode(root.right, temp.data)

        return root

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def PreOrder(self, root):
        if root:
            self.PreOrder(root.left)
            print(root.data, end=" -> ")
            self.PreOrder(root.right)

    def search(self, root, key):
        if root is None or root.data == key:
            return "Found" if root else "Not Found"

        if key < root.data:
            return self.search(root.left, key)
        
        else:
            return self.search(root.right, key)

tree = BST()
key = 99999
root = tree.createNode(765)
print(root.data)
root = tree.insert(root, 425)
root = tree.insert(root, 53)
root = tree.insert(root, 513)
root = tree.insert(root, 55)
root = tree.insert(root, 79)

print(tree.search(root, key))
tree.PreOrder(root)
print(None)
root = tree.deleteNode(root, 53)
tree.PreOrder(root)
print(None)

print(tree.minValueNode(root).data)