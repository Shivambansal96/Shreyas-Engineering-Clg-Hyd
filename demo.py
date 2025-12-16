# # # class Stack:
# # #     def __init__(self):
# # #         self.items = []

# # #     def push(self, value):
# # #         self.items = [value] + self.items

# # #     def pop(self):
# # #         print(self.items.pop())

# # #     def peek(self):
# # #         print(self.items[-1])

# # #     def isEmpty(self):
# # #         print(len(self.items) == 0)

# # #     def printStack(self):
# # #         print(f"Stack = {self.items}")


# # # s1 = Stack()

# # # s1.push(5)
# # # s1.push(35)
# # # s1.push(3135)
# # # s1.pop()
# # # s1.peek()
# # # s1.pop()
# # # s1.pop()
# # # s1.isEmpty()
# # # s1.printStack()





# # # def isValid(s):
# # #     Stack = []
# # #     myDict = { ')': '(', '}':'{', ']':'[' }

# # #     for char in s:
# # #         if char in myDict:
# # #             if Stack and Stack[-1] == myDict[char]:
# # #                 Stack.pop()

# # #             else:
# # #                 return False
                
# # #         else:
# # #             Stack.append(char)

# # #     return True if not Stack else False

# # # s = "()[]{}"
# # # print(isValid(s))

# # def infixToPostfix(s):
# #     outputValue = []
# #     stack = []
# #     priorityList = { '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# #     for char in s:
# #         if char == ' ':
# #             continue 
            
# #         if(char == '('):
# #             stack.append(char)
        
# #         elif(char == ')'):
# #             while stack and (stack[-1] != '('):
# #                 poppedValue = stack.pop()
# #                 outputValue.append(poppedValue)

# #             stack.pop()

# #         elif(char == '^' or char == '*' or char == '/' or char == '+' or char == '-'):
# #             while stack and (priorityList[stack[-1]] >= priorityList[char]):
# #                 poppedValue = stack.pop()
# #                 outputValue.append(poppedValue)

# #             stack.append(char)

# #         else:
# #             outputValue.append(char)  

# #     while(len(stack) != 0):
# #         poppedValue = stack.pop()
# #         outputValue.append(poppedValue)
            

# #     for i in s:
# #         print(i, end="")

# #     print()

# #     for i in outputValue:
# #         print(i, end="")



# # # s = input()
# # # s = "A + B / C - D"
# # s = "a+b*(c^d-e)^(f+g*h)-i"
# # infixToPostfix(s)




# # def nextGreaterElement(arr):
    
# #     stack = []
# #     ans = [-1] * len(arr)

# #     for i in range(len(arr)-1, -1, -1):

# #         while( stack and stack[-1] < arr[i]):
# #             stack.pop()

# #         if stack:
# #             ans[i] = stack[-1]

# #         stack.append(arr[i])

# #     print(ans)

# # arr = [1, 4, 5, 1, 3, 5, 6]
# # nextGreaterElement(arr)


# class Queue:
#     def __init__(self):
#         self.items = []

#     def enqueue(self, data):
#         self.items.append(data)

#     def deque(self):
#         first = self.items.pop(0)
#         print("Element Popped =", first)
#         return self.items




# q1 = Queue()

# q1.enqueue(4)
# q1.enqueue(324)
# q1.enqueue(44)
# q1.enqueue(31)

# print(q1.items)
# q1.deque()

# print(q1.items)



#-----------------------------------------#

# def postfixToInfix(s):
#     stack = []

#     for char in s:
#         if char == ' ':
#             continue

#         if char.isalnum():
#             stack.append(char)
        
#         else:

#             op1 = stack.pop()
#             op2 = stack.pop()

#             newStr = f"({op2}{char}{op1})"

#             stack.append(newStr)

#     return stack[-1]

# s = "A B C * +"
# print(postfixToInfix(s))

# ----------------------------------- #

# def moveZeroes(arr):
#     i = j = 0
#     n = len(arr)

#     while j < n:

#         if(arr[j] != 0):
#             arr[i], arr[j] = arr[j], arr[i]
#             i+=1 
#             j+=1

#         else:
#             j+=1

#     print(arr)


# arr = [1, 3, 0, 0, 1, 1, 12, 0]
# moveZeroes(arr)

# ----------------------------------------- #


# area = min(height[left], height[right]) * right - left


# def trapWater(arr):
#     left = 0
#     right = len(arr) - 1
#     maxArea = 0

#     while(left <= right):
#         width = right - left
#         minHeight = min(arr[left], arr[right])
#         area = minHeight * width

#         maxArea = max(maxArea, area)

#         if(arr[left] < arr[right]):
#             left+=1
#         else:
#             right -= 1


#     return maxArea

# arr = [1,8,6,2,5,4,8,3,7]
# print(f"Max Area = {trapWater(arr)}")



# ------------------------------------- #   


# def longestSubstring(s):
#     left = 0
#     right = 0
#     longest = 0
#     newSet = set()

#     # for i in range(len(s)):
#     while(right < len(s)):
#         while (s[right] in newSet):
#             newSet.remove(s[left])
#             left += 1

#         window = (right - left) + 1 
#         longest = max(longest, window)
#         newSet.add(s[right])
#         right += 1

#     return longest

# s = "abcabcbb"
# print(longestSubstring(s))


# --------------------------- #

# def maxAvg(arr):
#     currentSum = 0
#     k = 4

#     for i in range(k):
#         currentSum += arr[i]

#     max_avg = currentSum / k

#     for i in range(k, len(arr)):
#         currentSum += arr[i]
#         currentSum -= arr[i - k]

#         avg = currentSum / k

#         max_avg = max(max_avg, avg)


#     return max_avg

# arr = [1, 12, -5, -6, 50, 4]
# print(maxAvg(arr))


# -------------------------------- #
# class queue:
#     def __init__(self):
#         self.queue = []
#         self.size = 0

#     def enqueue(self, data):
#         self.queue += [data]
#         self.size += 1

#     def dequeue(self):
#         front = self.queue[0]
#         print(f"Dequeued = {front}")
#         self.queue = self.queue[1:]
#         return self.queue
    
#     def printQueue(self):
#         return " <- ".join(map(str, self.queue))

# q1 = queue()

# q1.enqueue(4)
# q1.enqueue(314)
# q1.enqueue(43)
# q1.enqueue(31)

# # print(q1.queue)
# print(q1.printQueue())

# q1.dequeue()
# q1.dequeue()
# q1.dequeue()

# print(q1.printQueue())

# -------------------------------- #


# class deque:
#     def __init__(self):
#         self.deque = []
#         self.size = 0

#     def prepend(self, data):
#         self.deque = [data] + self.deque
#         self.size += 1

#     def appendEnd(self, data):
#         self.deque = self.deque + [data]
#         self.size += 1

#     def removeStart(self):
#         front = self.deque[0]
#         print(f"Dequeued = {front}")
#         self.deque = self.deque[1:]
#         self.size -= 1

#         return self.deque

#     def removeEnd(self):
#         last = self.deque[self.size - 1]
#         print(f"Dequeued = {last}")
#         self.deque = self.deque[0:last]
#         self.size -= 1

#         return self.deque
    
#     def isEmpty(self):
#         return len(self.deque == 0)
    

# q1 = deque


# ------------------------------------- #

def twoSum(n, arr, target):
  left = 0
  right = n - 1
  
  while(left <= right):
    ans = arr[left] + arr[right]
    
    if(ans == target):
      return (left, right)
      
    elif(ans < target):
      left += 1
      
    else:
      right -= 1
      
      
  return (-1,)
    
    
    

# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
n = 5
arr = [2, 7, 11, 15, 20]
target = 90
tup = twoSum(n, arr, target)

for i in tup:
  print(i, end=" ")