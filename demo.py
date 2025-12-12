# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, value):
#         self.items = [value] + self.items

#     def pop(self):
#         print(self.items.pop())

#     def peek(self):
#         print(self.items[-1])

#     def isEmpty(self):
#         print(len(self.items) == 0)

#     def printStack(self):
#         print(f"Stack = {self.items}")


# s1 = Stack()

# s1.push(5)
# s1.push(35)
# s1.push(3135)
# s1.pop()
# s1.peek()
# s1.pop()
# s1.pop()
# s1.isEmpty()
# s1.printStack()





# def isValid(s):
#     Stack = []
#     myDict = { ')': '(', '}':'{', ']':'[' }

#     for char in s:
#         if char in myDict:
#             if Stack and Stack[-1] == myDict[char]:
#                 Stack.pop()

#             else:
#                 return False
                
#         else:
#             Stack.append(char)

#     return True if not Stack else False

# s = "()[]{}"
# print(isValid(s))

def infixToPostfix(s):
    outputValue = []
    stack = []
    priorityList = { '(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in s:
        if char == ' ':
            continue 
            
        if(char == '('):
            stack.append(char)
        
        elif(char == ')'):
            while stack and (stack[-1] != '('):
                poppedValue = stack.pop()
                outputValue.append(poppedValue)

            stack.pop()

        elif(char == '^' or char == '*' or char == '/' or char == '+' or char == '-'):
            while stack and (priorityList[stack[-1]] >= priorityList[char]):
                poppedValue = stack.pop()
                outputValue.append(poppedValue)

            stack.append(char)

        else:
            outputValue.append(char)  

    while(len(stack) != 0):
        poppedValue = stack.pop()
        outputValue.append(poppedValue)
            

    for i in s:
        print(i, end="")

    print()

    for i in outputValue:
        print(i, end="")



# s = input()
# s = "A + B / C - D"
s = "a+b*(c^d-e)^(f+g*h)-i"
infixToPostfix(s)