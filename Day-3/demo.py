# # class Student:
# #     # name = "Shivam"
# #     # marks = 980

# #     clgName= "SEC"
# #     branch = "CSE"
# #     Year = "3"

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.__age = age
# #         self.welcomeMsg()

# #     @staticmethod
# #     def __welcomeMsg():
# #         print(f"Welcome!!")

# # s1 = Student("Shivam", 424)
# # print(s1.__age)
# # # print(s1)
# # # print(s1.marks)

# # print("-------------------------")

# # s2 = Student("Kartik", 536)
# # # print(s2)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def printList(self):
#         current = Node1

#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print(None)

# Node1 = Node(43)
# Node2 = Node(54)
# Node3 = Node(10)
# # NodeMid = Node(25)


# Node1.next = Node2
# Node1.next.next = Node3

# # Node1.next = Node2
# # Node2.next = Node3

# # NodeMid.next = Node3
# # Node2.next = NodeMid


# # Node1.next = NodeMid
# Node1.printList()


# ------------------------------------------------------- #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendElement(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

    def appendAtStart(self, data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    # def appendAtPosLocation(self, data, pos):
        
    #     if pos < 0 or pos > self.length:
    #         print(f"Invalid position: {pos}. Valid range is 0 to {self.length}")
    #         return

    #     if(pos == self.length):
    #         self.appendElement(data)

    #     elif(pos == 0):
    #         self.appendAtStart(data)

    #     else:
    #         current = self.head
    #         newNode = Node(data)

    #         for i in range(pos-1):
    #             current = current.next

    #         newNode.next = current.next
    #         current.next = newNode
#         self.length += 1

    def appendAnywhere(self, data, pos):
        
        if(pos == self.length):
            self.appendElement(data)
        
        elif(pos == 0):
            self.appendAtStart(data)

        else:
            current = self.head
            newNode = Node(data)
            
            for i in range(pos-1):
                current = current.next
                
            newNode.next = current.next
            current.next = newNode
            
        self.length += 1
        



    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print(None)


newList = LinkedList()
# newList.appendElement(5)
# newList.appendAtStart(54)
newList.appendElement(1)
newList.appendElement(2)
newList.appendAnywhere(2, 3)
# newList.appendElement()
newList.appendElement(4)
newList.appendElement(5)
# newList.appendElement(754)

newList.printLinkedList()


        





