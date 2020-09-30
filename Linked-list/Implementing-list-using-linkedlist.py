class node:
    def __init__(self,info):
        self.info = info
        self.next = None
class linkedlist():
    def __init__(self):
        self.root = None
    def append(self, val):
        current = self.root
        if current is None:
            self.root = node(val)
        else:
            while current.next:
                current = current.next
            current.next = node(val)
    def countll(self,val):
        current = self.root
        count = 0
        while current:
            if(current.info == val):
                count += 1
            current = current.next
        return count
    def indexll(self,val,*args):
        current = self.root
        if(len(args)):
            no = args[0]
            count = 0
            inde = 0
            while current:
                if(current.info == val):
                    count += 1
                    if(count == no):
                        ans = inde
                        break
                inde += 1
                current = current.next
        else:
            current = self.root
            count = 0
            while(current):
                if(current.info == val):
                    ans = count
                    break
                count += 1
                current = current.next
        return ans
    def popll(self, *args):
        if (len(args)):
            val = args[0]
            current = self.root
            while (current.info != val):
                pre = current
                current = current.next
            pre.next = current.next
        else:
            current = self.root
            while (current.next):
                pre = current
                current = current.next
            pre.next = None
    def reversell(self):
        current = self.root
        pre = None
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.root = pre
def sortll(lis):
    current = lis.root
    while(current.next):
        next_is = current.next
        while(next_is):
            if(current.info > next_is.info):
                current.info,next_is.info = next_is.info,current.info
            next_is = next_is.next
        current = current.next
def maxll(lis):
    current = lis.root
    big = 0
    while current:
        if(current.info > big):
            big = current.info
        current = current.next
    return big
def minll(lis):
    current = lis.root
    small = 99999999999999999999999999
    while current:
        if(current.info < small):
            small = current.info
        current = current.next
    return small
def lenll(lis):
    current = lis.root
    count = 0
    while current:
        count += 1
        current = current.next
    return count
def sumll(lis):
    sumi = 0
    current = lis.root
    while current:
        sumi += current.info
        current = current.next
    return sumi
def printll(lis):
    current = lis.root
    print("[",end = "")
    while current:
        if(current.next == None):
            print(str(current.info),end = "")
        else:
            print(str(current.info), end=",")
        current = current.next
    print("]")
lis = [5,6,3,2,7,6]
l = linkedlist()
printll(l)
for i in lis:
    l.append(i)
print("Printing the linked list")
printll(l)
print("The sum of the linked list is ",end = "")
print(sumll(l))
print("The length of the linked list is ",end = "")
print(lenll(l))
print("The position of a given number is",end = " ")
print(l.indexll(6,2))
print("The maximum value of the linked list is ",end = "")
print(maxll(l))
print("The minimum value of the linked list is ",end = "")
print(minll(l))
sortll(l)
print("The sorted linked list is",end = " ")
printll(l)
l.reversell()
print("The reversed linked list is",end = " ")
printll(l)