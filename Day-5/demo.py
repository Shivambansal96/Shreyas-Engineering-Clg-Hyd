

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, value):
#         self.items = self.items + [value]
#         print(f"{value} pushed into the stack")

#     def pop(self):
#         if self.isEmpty():
#             return "Stack is Empty!!"
#         else:

#             ele = self.items.pop()
#             print(f"{ele} is removed from the stack")

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is Empty!!"
#         else:
#             print(f"{self.items[-1]} is at the top")

#     def isEmpty(self):
#         if len(self.items) == 0:
#             return True
#         else:
#             return False
        
#     def printStack(self):
#         return (f"Stack = {self.items}")
        

# s1 = Stack()

# # s1.push(4)
# # s1.push(48)
# # s1.push(31)
# # s1.peek()
# # s1.pop()
# # s1.pop()
# # s1.pop()
# # s1.peek()
# # print(s1.isEmpty())

# # print(s1.printStack())

# # --------------------------------------------------------- #

# # # # # # Stack implementation with Capacity / Size

# # class Stack:
# #     def __init__(self, size):
# #         self.size = size
# #         self.stack = [None] * size
# #         self.top = -1

# #     def isEmpty(self):
# #         return self.top == -1

# #     def isFull(self):
# #         return self.top == self.size - 1

# #     def push(self, value):
# #         if self.isFull():
# #             print(f"Stack Overflow, New Value = {value}")
        
# #         else:
# #             self.top += 1
# #             self.stack[self.top] = value
# #             print(f"Pushed: {value}")

# #     def pop(self):
# #         if self.isEmpty():
# #             print(f"Stack Underflow! Nothing to remove.")

# #         else:
# #             ele = self.stack[self.top]
# #             self.stack[self.top] = None
# #             self.top -= 1
# #             print(f"Element popped: {ele}")
# #             return ele
        
# #     def peek(self):
# #         if self.isEmpty():
# #             print("Stack is already Empty!!")
# #             return

# #         return self.stack[self.top]
    
# #     def printStack(self):
# #         print("Stack: ", end="")
# #         for i in self.stack[::-1]:
# #             if i != None:
# #                 print(i, end=" ")


# #     def reversedList(self):
# #         reversedList = []

# #         while(self.size):
# #             ele = self.pop()
# #             reversedList.append(ele)

# #             self.size -= 1
        
# #         print(f"Reversed List = {reversedList}")


# # s1 = Stack(5)
# # # s1.push(53)
# # # s1.push(353)
# # # s1.push(3)
# # # s1.push(1)
# # # print(f"Top Element = {s1.peek()}")
# # # s1.pop()
# # # print(f"Top Element = {s1.peek()}")

# # # # print(s1.stack)
# # # s1.printStack()


# # # s1.push(1)
# # # s1.push(2)
# # # s1.push(3)
# # # s1.push(4)
# # # s1.push(5)

# # # s1.reversedList()


# def isValid(s):

#     Stack = []
#     listOfBrackets = {')' : '(', '}': '{', ']': '['}

#     # if(s[0] == ')' or s[0] == '}' or s[0] == ']'):
#     #     return False

#     count = 0
#     for char in s:
#         count += 1
#         print(count)


#         if char in listOfBrackets:
#             if Stack and Stack[-1] == listOfBrackets[char]:
#                 Stack.pop()

#             else:
#                 return False

#         else:
#             Stack.append(char)


#     return True if not Stack else False

    

# s = ")()[]"
# print(isValid(s))
# # print(isValid(s))



def hasDuplicates(s):

    stack = []

    count = 0
    for char in s:
        if(char == ')'):

            while stack[-1] != '(':
                stack.pop()
                count += 1

            if stack:
                stack.pop()

        else:
            stack.append(char)

        

s = "(a+(b))"
print(hasDuplicates(s))