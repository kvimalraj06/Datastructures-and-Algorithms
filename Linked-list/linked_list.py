class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def length(self):
        currentnode=self.head
        length=0
        while currentnode.next!=None:
            length +=1
            currentnode=currentnode.next
        return length
    def insert(self,newnode):
        if self.head == None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if(lastnode.next==None):
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def printlist(self):
        if self.head==None:
            print("list is empty")
        else:
            currentnode=self.head
            while True:
                if currentnode == None:
                    break
                print(currentnode.data,end=" ")
                currentnode=currentnode.next
            print()
    def inserthead(self,data):
        tempnode=self.head
        self.head=data
        data.next=tempnode
        del tempnode
    def insertAt(self,data, position):
        if (position <0 or position > self.length()):
            print("list index out of range")
            return
        if position ==0:
            self.inserthead(data)
            return
        else:
            currentnode=self.head
            currentpos = 0
            while True:
                if(currentpos==position):
                    previousnode.next=data
                    data.next=currentnode
                    break
                else:
                    previousnode=currentnode
                    currentnode=currentnode.next
                    currentpos += 1
    def deleteEnd(self):
        currentnode=self.head
        while True:
            if currentnode.next==None:
                previousnode.next=None
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
    def deleteAt(self,position):
        if(position < 0 or position > self.length()):
            print("list index out of range")
        else:
            currentnode=self.head
            currentpos=0
            while True:
                if(currentpos==position):
                    previous.next=currentnode.next
                    break
                else:
                    previous=currentnode
                    currentnode=currentnode.next
                    currentpos += 1








