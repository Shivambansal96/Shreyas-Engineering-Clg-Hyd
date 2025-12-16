# # class Queue:
# #     def __init__(self):
# #         self.queue = []
# #         self.length = 0

# #     def enqueue(self, data):
# #         self.queue = self.queue + [data]
# #         self.length += 1

# #     def dequeue(self):
# #         front = self.queue[0]
# #         print(f"Dequeued = {front}")
# #         self.queue =  self.queue[1:]
# #         self.length -= 1

# #         return self.queue
    
# # q1 = Queue()
# # q1.enqueue(42)
# # q1.enqueue(22)
# # q1.enqueue(2)
# # print(q1.queue)
    
# # q1.dequeue()
# # q1.dequeue()
# # print(q1.queue)


# class Dequeue:
#     def __init__(self):
#         self.deque = []
#         self.length = 0

#     def prepend(self, data):
#         self.deque = [data] + self.deque 
#         self.length += 1

#     def appendEnd(self, data):
#         self.deque = self.deque + [data]
#         self.length += 1

#     def deleteFirst(self):
#         front = self.deque[0]
#         print(f"Dequeued = {front}")
#         self.deque = self.deque[1:]
#         self.length -= 1

#         return self.deque

#     def deleteEnd(self):
#         last = self.deque[-1]
#         print(f"Dequeued = {last}")
#         self.deque = self.deque[:len(self.deque) - 1]
#         self.length -= 1

#         return self.deque



def postfixToInfix(s):
    stack = []
    stack.remove()
    for char in s:
        if char.isalnum():
            stack.append(char)

        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            newStr = (f"({operand2}{char}{operand1})")

            stack.append(newStr)

    # return stack[0]
    return stack[-1]


    

s = "ABC*+"
print(postfixToInfix(s))
