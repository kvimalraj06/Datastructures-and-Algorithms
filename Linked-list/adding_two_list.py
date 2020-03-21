"""
input list1:1->2->3->4->None
input list2:3->4->5->None

output = 1->5->7->9->None

logic:(1234 + 345 = 1579)
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            lastnode = self.head
            while lastnode.next != None:
                lastnode = lastnode.next
            lastnode.next = newnode

    def printlist(self):
        if self.head == None:
            print("The list if fucking empty")
        else:
            start_node = self.head
            while start_node.next != None:
                print(start_node.data,end="->")
                start_node = start_node.next
            print(start_node.data,end="->None")
            print()

    def length(self):
        len = 1
        startnode = self.head
        while startnode.next != None:
            len+=1
            startnode = startnode.next
        return len

    def reverselist(self):
        previousnode = None
        presentnode = self.head
        while presentnode.next != None:
            nextnode = presentnode.next
            presentnode.next = previousnode
            previousnode = presentnode
            presentnode = nextnode
        presentnode.next = previousnode
        self.head = presentnode

    def insert(self, newnode):
        newnode=Node(newnode)
        if self.head == None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if(lastnode.next==None):
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def add_two_list(self,lis1,lis2):
        lis1.reverselist()
        lis2.reverselist()
        lis1_length = lis1.length()
        lis2_length = lis2.length()
        if lis1_length < lis2_length:
            small_lis = lis1
            large_lis = lis2
        else:
            small_lis = lis2
            large_lis = lis1
        start_node1 = large_lis.head
        start_node2 = small_lis.head
        reminder = 0
        for i in range(large_lis.length()):
            if i < small_lis.length():
                start_node1.data = start_node1.data + start_node2.data + reminder
                if start_node1.data//10 !=0:
                    reminder = start_node1.data//10
                    start_node1.data = start_node1.data%10
                    start_node1 = start_node1.next
                    start_node2 = start_node2.next
                else:
                    reminder = 0
                    start_node1 = start_node1.next
                    start_node2 = start_node2.next
            else:
                start_node1.data = start_node1.data + reminder
                if start_node1.data//10 != 0:
                    reminder = start_node1.data//10
                    start_node1.data = start_node1.data % 10
                    start_node1 = start_node1.next
                else:
                    reminder = 0
                    break
        if reminder:
            large_lis.insert(reminder)
        lis1.reverselist()
        lis1.printlist()

lis1 = LinkedList()
lis2 = LinkedList()
lis1.insert(1)
lis1.insert(2)
lis1.insert(3)
lis1.insert(4)
lis1.printlist()
lis2.insert(3)
lis2.insert(4)
lis2.insert(5)
lis2.printlist()
lis1.add_two_list(lis1, lis2)



