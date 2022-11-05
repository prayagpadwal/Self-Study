# Creating node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # address of the next node

# Creating SSL
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_middle(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

# Display the SSL
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end = " ")
                temp = temp.next # moves to the next node

# Calling objects 
link = SingleLinkedList()
n1 = Node(10) # data in first node as 10
link.head = n1
n2  = Node(20) # data in second node as 20
link.head.next = n2
n3 = Node(30) # data in third node as 30
n2.next = n3  
n4 = Node(40) # data in fourth node as 40
n3.next = n4
link.insert_begining(5)
link.insert_end(60)
link.insert_middle(3, 25)

link.display() #display the linked list

