# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None

# # class BST:
# #     def createNode(self, data):
# #         return Node(data)
    
# #     def insert(self, root, data):
# #         if root is None:
# #             return self.createNode(data)

# #         if data < root.data:
# #             root.left = self.insert(root.left, data)
# #         else:
# #             root.right = self.insert(root.right, data)

# #         return root
    
# #     def deleteNode(self, root, key):
# #         if root is None:
# #             return root

# #         if key < root.data:
# #             root.left = self.deleteNode(root.left, key)
        
# #         elif key > root.data:
# #             root.right = self.deleteNode(root.right, key)
        
# #         else:
# #             # Node with only one child or no child
                
# #             if root.left is None:
# #                 return root.right
# #             elif root.right is None:
# #                 return root.left

# #             # Node with two children: Get the in order successor (smallest in the right subtree)
# #             # temp = self.minValueNode(root.left) # Doesn't matter what you choose for two children
# #             temp = self.minValueNode(root.right)


# #             # Copy the in order successor's content to this node
# #             root.data = temp.data

# #             # Delete the In order successor
# #             root.right = self.deleteNode(root.right, temp.data)

# #         return root

# #     def minValueNode(self, node):
# #         current = node
# #         while current.left is not None:
# #             current = current.left
# #         return current
    
# #     def PreOrder(self, root):
# #         if root:
# #             self.PreOrder(root.left)
# #             print(root.data, end=" -> ")
# #             self.PreOrder(root.right)

# #     def search(self, root, key):
# #         if root is None or root.data == key:
# #             return "Found" if root else "Not Found"

# #         if key < root.data:
# #             return self.search(root.left, key)
        
# #         else:
# #             return self.search(root.right, key)

# # tree = BST()
# # key = 99999
# # root = tree.createNode(765)
# # print(root.data)
# # root = tree.insert(root, 425)
# # root = tree.insert(root, 53)
# # root = tree.insert(root, 513)
# # root = tree.insert(root, 55)
# # root = tree.insert(root, 79)

# # print(tree.search(root, key))
# # tree.PreOrder(root)
# # print(None)
# # root = tree.deleteNode(root, 53)
# # tree.PreOrder(root)
# # print(None)

# # print(tree.minValueNode(root).data)



# # # # Adjacency Matrix Representation of Graph # #

# # n = 8
# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]

# # graph = []

# # for i in range(n):
# #     graph.append([0] * n)

# # print('[')
# # print(',\n'.join(map(str, graph)))
# # print(']')

# # for i, j in arr:
# #     graph[i][j] = 1

# # print('[')
# # print(',\n'.join(map(str, graph)))
# # print(']')

# # # For unidirectional

# # for i, j in arr:
# #     graph[j][i] = 1

# # print('[')
# # print(',\n'.join(map(str, graph)))
# # print(']')

# # # # Adjacency List Representation of Graph (defaultDict)# #

# # from collections import defaultdict

# # n = 8
# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]

# # D = defaultdict(list)

# # for i, j in arr:
# #     D[i].append(j)

# # # print(dict(D))


# # def dfsRecursive(node):
# #     print(node, end=" ")

# #     for nei_node in D[node]:
# #         if nei_node not in seen:
# #             seen.add(nei_node)
# #             dfsRecursive(nei_node)

# # source = 0

# # seen = set()
# # seen.add(source)
# # print("Recursive ", end=" -> ")
# # dfsRecursive(source)
# # print()


# # # # Iterative DFS # # # 

# # from collections import defaultdict

# # D = defaultdict(list)

# # n = 8
# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]

# # for i, j in arr:
# #     D[i].append(j)

# # # print(dict(D))

# # source = 0
# # seen = set()
# # stack = [source]
# # print("Iterative ", end=" -> ")

# # while stack:
# #     node = stack.pop()

# #     print(node, end=" ")

# #     for neighbor in reversed(D[node]):
# #         if neighbor not in seen:
# #             seen.add(neighbor)
# #             stack.append(neighbor)


# # # # # BFS using deque # # # # 

# # from collections import deque, defaultdict

# # D = defaultdict(list)

# # n = 8
# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]

# # for i, j in arr:
# #     D[i].append(j)

# # source = 0
# # seen = set()
# # seen.add(source)

# # q = deque()
# # q.append(source)

# # while q:
# #     node = q.popleft()

# #     print(node, end=" ")

# #     for neighbor in D[node]:
# #         if neighbor not in seen:
# #             seen.add(neighbor)
# #             q.append(neighbor)

# # # # Recursive DFS # # 


# def dfsRecursive(node):
#     seen[node] = True

#     dfs.append(node)

#     for neighbor in arr[node]:
#         if not seen[neighbor]:
#             dfsRecursive(neighbor)

# n = 8
# arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]
# source = 0
# seen = [False] * len(arr)
# dfs = []

# dfsRecursive(source)
# print(dfs)



# # # # # # Manual Connection of Nodes # #  #
# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.neighbors = []

# #     def display(self):
# #         connections = []
# #         for node in self.neighbors:
# #             connections.append(node.value)

# #         return f"{self.value} is connected to {connections}"
    
# # A = Node('A')
# # B = Node('B')
# # C = Node('C')
# # D = Node('D')
        
# # A.neighbors.append(B)
# # B.neighbors.append(A)
# # C.neighbors.append(D)
# # D.neighbors.append(C)

# # print(A.display())
# # print(B.display())
# # print(C.display())
# # print(D.display())








# # import ast
# # from collections import deque, defaultdict



# # # arr = ast.literal_eval(input())
# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]


# # D = defaultdict(list)
# # source = 0
# # seen = set()
# # seen.add(source)

# # q = deque()
# # q.append(source)
# # newArr = []

# # for i, j in arr:
# #   D[i].append(j)

# # while q:
# #   node = q.popleft()
# #   newArr.append(node)

# #   for neighbor in D[node]:
    
# #     if neighbor not in seen:
# #       seen.add(neighbor)
# #       q.append(neighbor)

# # print(newArr)




# # from collections import deque, defaultdict

# # q = deque()
# # D = defaultdict(list)

# # arr = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 5], [5, 2]]

# # for i, j in arr:
# #     D[i].append(j)

# # source = 0
# # # visited = [False] * len(arr)
# # visited = set()
# # q.append(source)

# # while q:
# #     node = q.popleft()

# #     print(node)

# #     for neighbour in D[node]:

# #         if neighbour not in visited:
# #             q.append(neighbour)
# #             # visited[neighbour] = True
# #             visited.add(neighbour)
