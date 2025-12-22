

# n = 8  # Vertices

# arr = [[0,1], [1, 2],[0,3], [3,4], [4, 5], [3, 6], [3,7], [5,8] ]

# graph = []

# for i in range(n):
#     graph.append([0] * n)

# # # # Directed Graph
# for u, v in arr:
#     graph[u][v] = 1

# # # # UnDirected Graph
# for u, v in arr:
#     graph[u][v] = 1
#     graph[v][u] = 1

# print('[')
# print("\n".join(map(str, graph)))
# print(']')


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.neighbours = []

#     def display(self):
#         connections = []

#         for node in self.neighbours:
#             connections.append(node.data)

#         print(f"{self.data} is connected to {connections}")

# A = Node('A')
# B = Node('B')
# C = Node('C')
# D = Node('D')
# E = Node('E')

# D.neighbours.append(A)
# D.neighbours.append(E)
# A.neighbours.append(B)
# B.neighbours.append(C)
# C.neighbours.append(D)

# D.display()


# # # # DFS Recursive Method # # # #

from collections import defaultdict

V = 8
# arr = [[0,1], [1, 2],[0,3], [3,4], [4, 5], [3, 6], [3,7], [5,3] ]
arr = [[0, 1], [0,2], [1, 3], [2, 4], [2, 3], [3, 4]]

D = defaultdict(list)

for i, j in arr:
    D[i].append(j)
    D[j].append(i)
    

def dfsRecursive(node):
    print(node, end=" ")

    for neighbour in D[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            dfsRecursive(neighbour)

source = 0
visited = set()
visited.add(source)
# dfsRecursive(source)

stack = [source]

while stack:
    node = stack.pop()

    print(node, end=" ")

    for neighbour in reversed(D[node]):
        if neighbour not in visited:
            visited.add(neighbour)
            stack.append(neighbour)






# for i, j in D.items():
#     print(f"{i} : {j}")

# # print(dict(D))
