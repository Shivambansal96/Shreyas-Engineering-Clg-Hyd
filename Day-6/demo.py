
# def infixToPostfix(s):
#     outputValue = []
#     stack = []
#     priorityList = { '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

#     for char in s:
#         if char == ' ':
#             continue 
            
#         if(char == '('):
#             stack.append(char)
        
#         elif(char == ')'):
#             while stack and (stack[-1] != '('):
#                 poppedValue = stack.pop()
#                 outputValue.append(poppedValue)

#             stack.pop()

#         elif(char == '^' or char == '*' or char == '/' or char == '+' or char == '-'):
#             while stack and (priorityList[stack[-1]] >= priorityList[char]):
#                 poppedValue = stack.pop()
#                 outputValue.append(poppedValue)

#             stack.append(char)

#         else:
#             outputValue.append(char)  

#     while(len(stack) != 0):
#         poppedValue = stack.pop()
#         outputValue.append(poppedValue)
            

#     for i in s:
#         print(i, end="")

#     print()

#     for i in outputValue:
#         print(i, end="")



# # s = input()
# # s = "A + B / C - D"
# s = "a+b*(c^d-e)^(f+g*h)-i"
# infixToPostfix(s)




# def nextGreaterElement(arr):
    
#     stack = []
#     ans = [-1] * len(arr)

#     for i in range(len(arr)-1, -1, -1):

#         while( stack and stack[-1] < arr[i]):
#             stack.pop()

#         if stack:
#             ans[i] = stack[-1]

#         stack.append(arr[i])

#     print(ans)

# arr = [1, 4, 5, 1, 3, 5, 6]
# nextGreaterElement(arr)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def deque(self):
        first = self.items.pop(0)
        print("Element Popped =", first)
        return self.items




q1 = Queue()

q1.enqueue(4)
q1.enqueue(324)
q1.enqueue(44)
q1.enqueue(31)

print(q1.items)
q1.deque()

print(q1.items)
