# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
        
#     def appendElement(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode

#         else:
#             self.tail.next = newNode
#             self.tail = newNode

#         self.length += 1

#     def prepend(self, data):

#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
        
#         else:
#             newNode.next = self.head
#             self.head = newNode

#         self.length += 1

#     def insertAtPos(self, data, pos):
        
#         newNode = Node(data)

#         if(pos <= 0):
#             self.prepend(data)

#         elif(pos > self.length):
#             raise IndexError("Index out of Bounds!!")

#         else:
#             if(pos == self.length): 
#                 self.appendElement(data)

#             else:

#                 current = self.head
#                 for i in range(pos-1):
#                     current = current.next

#                 newNode.next = current.next
#                 current.next = newNode

#         self.length += 1


#     def deleteStart(self):
#         if self.head is None:
#             print("Linked List is Empty !!!")

#         else:
#             self.head = self.head.next

#         self.length -= 1

#     def deleteEnd(self):
#         if self.head is None:
#             print("Linked List is Empty !!!")
        
#         else:
        
#             current = self.head

#             if(self.length == 1):
#                 self.head = None
#                 self.tail = None

#             else:
#                 # while current.next.next:
#                 for i in range(1, self.length - 1):
#                     current = current.next

#                 current.next = None

#                 self.tail = current
        
#             self.length -= 1

#     def deleteAtPos(self, pos):

#         if self.head is None:
#             print("Linked List is Empty!!!")

#         else:
#             if(pos == 0):
#                 self.deleteStart()

#             elif(pos+1 == self.length):
#                 self.deleteEnd()

#             elif(pos >= self.length):
#                 raise IndexError(f"{pos} is out of Bounds.")

#             else:
#                 current = self.head

#                 for i in range(pos-1):
#                     current = current.next

#                 current.next = current.next.next
            
#             self.length -= 1


#     def deleteValue(self, data):
#         if self.head is None:
#             print("Linked List is Empty!!!")

#         else:

#             current = self.head

#             if(current.data == data):
#                 self.deleteStart()

#             else:

#                 for i in range(1, self.length - 1):
#                     print(current.next.data)
#                     if(i+2 == self.length):
#                         self.deleteEnd()

#                     if current.next.data == data: 
#                         # self.deleteAtPos(i+1)
#                         current.next = current.next.next

#                         self.length -= 1
                    
#                     current = current.next

#                 # else:
#                 #     print(f"{data} doesn't exist in the Linked List.")



#     def printLinkedList(self):
#         current = self.head

#         while current:
#             print(current.data, end=" -> ")
#             current = current.next

#         print(None)


# list1 = LinkedList()


# list1.printLinkedList()

# list1.appendElement(20)
# list1.appendElement(30)
# list1.prepend(10)

# list1.insertAtPos(25, 2)

# list1.printLinkedList()
# # list1.deleteStart()
# # list1.deleteEnd()
# list1.deleteValue(20)

# list1.printLinkedList()
# list1.reversedList()
# list1.printLinkedList()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
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

            newNode.prev = self.tail # Changed for DLL

            self.tail.next = newNode
            self.tail = newNode

            self.tail.next = self.head
            self.head.prev = self.tail



        self.length += 1

    def prepend(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        
        else:
            self.head.prev = newNode # Changed for DLL
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def insertAtPos(self, data, pos):
        
        newNode = Node(data)

        if(pos <= 0):
            self.prepend(data)

        elif(pos > self.length):
            raise IndexError("Index out of Bounds!!")

        else:
            if(pos == self.length): 
                self.appendElement(data)

            else:

                current = self.head
                for i in range(pos-1):
                    current = current.next
                    
                newNode.next = current.next

                newNode.prev = current
                current.next.prev = newNode
                current.next = newNode


        self.length += 1


    def deleteStart(self):
        if self.head is None:
            print("Linked List is Empty !!!")

        else:

            self.head.next.prev = None # Changed for DLL
            self.head = self.head.next

        self.length -= 1

    def deleteEnd(self):
        if self.head is None:
            print("Linked List is Empty !!!")
        
        else:
        
            current = self.head

            if(self.length == 1):
                self.head = None
                self.tail = None

            else:
                # while current.next.next:
                for i in range(1, self.length - 1):
                    current = current.next

                current.next = None

                self.tail = current
        
            self.length -= 1

    def deleteAtPos(self, pos):

        if self.head is None:
            print("Linked List is Empty!!!")

        else:
            if(pos == 0):
                self.deleteStart()

            elif(pos+1 == self.length):
                self.deleteEnd()

            elif(pos >= self.length):
                raise IndexError(f"{pos} is out of Bounds.")

            else:
                current = self.head

                for i in range(pos-1):
                    current = current.next

                current.next = current.next.next
            
            self.length -= 1


    def deleteValue(self, data):
        if self.head is None:
            print("Linked List is Empty!!!")

        else:

            current = self.head

            if(current.data == data):
                self.deleteStart()

            else:

                for i in range(1, self.length - 1):
                    print(current.next.data)
                    if(i+2 == self.length):
                        self.deleteEnd()

                    if current.next.data == data: 
                        # self.deleteAtPos(i+1)
                        current.next = current.next.next

                        self.length -= 1
                    
                    current = current.next

                # else:
                #     print(f"{data} doesn't exist in the Linked List.")



    def printLinkedList(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print(None)


    def printReversedLinkedList(self):
        current = self.tail

        while current:
            print(current.data, end=" -> ")
            current = current.prev

        print(None)


list1 = DoublyLinkedList()


list1.printLinkedList()

list1.appendElement(20)
list1.appendElement(30)
list1.appendElement(70)
list1.appendElement(170)
list1.prepend(10)

list1.insertAtPos(25, 2)

list1.printLinkedList()
list1.deleteStart()
# # list1.deleteEnd()
# list1.deleteValue(20)

# list1.printLinkedList()
# list1.printLinkedList()
list1.printReversedLinkedList()

