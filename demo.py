
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class LinkedList:
    def __init__(self):
        self.head = None    
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printing(self):
        if self.head is None:
            print(f"The linked list is None")
        else:
            current = self.head
            while current:
                print(current.data,end= "-> ")
                current = current.next
        

ll1 = LinkedList()
array = [10,20,30,40,50]
for i in array:
    ll1.append(i)


ll1.append(498)


ll1.printing()