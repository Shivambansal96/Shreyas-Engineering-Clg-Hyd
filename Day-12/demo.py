# # # # # BFS Iterative # # # 

# # # USING QUEUES

# from collections import defaultdict, deque

# arr = [ [5, 1], [5, 2], [1, 3], [2, 4], [2, 3], [3, 4] ]
# # arr = [ [0,2], [0, 1], [1, 3], [2, 4], [2, 3], [3, 4] ]



# D = defaultdict(list)
# q = deque()

# for u, v in arr:
#     D[u].append(v)
#     D[v].append(u) # Bi-directional

# source = arr[0][0]
# visited = set()
# visited.add(source)

# q.append(source)

# print("BFS Iterative -- >")

# while q:

#     node = q.popleft()

#     print(node, end=" ")

#     for neighbor in D[node]:
#         if neighbor not in visited:
#             q.append(neighbor)
#             visited.add(neighbor)

# print()

# # # # DFS Recursive # # #

# from collections import defaultdict, deque

# arr = [ [5, 1], [5, 2], [1, 3], [2, 4], [2, 3], [3, 4] ]
# # arr = [ [0,2], [0, 1], [1, 3], [2, 4], [2, 3], [3, 4] ]

# D = defaultdict(list)
# q = deque()

# for u, v in arr:
#     D[u].append(v)
#     # D[v].append(u) # Bi-directional

# visited = set()
# source = arr[0][0]
# visited.add(source)
# print("DFS Recursive -- >")


# def dfsRecursive(node):
#     print(node, end=" ")

#     for neighbor in D[node]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             dfsRecursive(neighbor)

# dfsRecursive(source)
# print()




# # # # DFS Iterative # # #

# from collections import defaultdict

# arr = [ [5, 1], [5, 2], [1, 3], [2, 4], [2, 3], [3, 4] ]
# # arr = [ [0,2], [0, 1], [1, 3], [2, 4], [2, 3], [3, 4] ]

# D = defaultdict(list)

# for u, v in arr:
#     D[u].append(v)
#     # D[v].append(u) # Bi-directional

# visited = set()
# source = arr[0][0]
# stack = [source]
# visited.add(source)
# print("DFS Iterative -- >")

# while stack:

#     node = stack.pop()

#     print(node, end=" ")

#     for neighbor in reversed(D[node]):
#         if neighbor not in visited:
#             visited.add(neighbor)
#             stack.append(neighbor)



# # # Cycle Detection # # # 


from collections import defaultdict

n = 5
# arr = [ [0, 1], [0, 2], [1, 3], [2, 4], [2, 3], [3, 4] ]
arr = [ [0,2], [0, 1], [1, 3], [2, 4], [2, 3], [3, 4], [3, 0] ]

D = defaultdict(list)

for u, v in arr:
    D[u].append(v)
    # D[v].append(u) # Bi-directional
    
Unvisited = 0
Visiting = 1
Visited = 2

states = [Unvisited] * n

def AcyclicDetection(node):
    if states[node] ==  Visiting:
        return False
    elif states[node] == Visited:
        return True
    
    states[node] = Visiting

    for neighbor in D[node]:
        if not AcyclicDetection(neighbor):
            return False
    
    states[node] = Visited
    return True

for i in range(n):
    if states[i] == Unvisited:
        if not AcyclicDetection(i):
            print("Cycle Detected")
            break
else:
    print("No Cycle Detected")




