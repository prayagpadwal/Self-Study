# Creating node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # address of the next node

# Creating SSL
class SingleLinkedList:
    def __init__(self):
        self.head = None

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
link.head.next = n3
link.display()
