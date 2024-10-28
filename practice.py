class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class LL:
    def __init__(self):
        self.head=None 


    def print(self):
        temp=self.head 
        while temp != None:
            print(temp.data,end="->")
            temp=temp.next

    def addFront(self,data):
        NewNode=Node(data)
        NewNode.next=self.head 
        self.head=NewNode 
    def addLast(self,data):
        NewNode=Node(data) 
        if self.head is  None:
            self.head=NewNode
            return 
        temp=self.head 
        while temp.next != None:
            temp=temp.next 
        temp.next=NewNode 

    def deleteFirst(self):
        if self.head is None: 
            print("linkedlist is empty")
        else:
            self.head=self.head.next 
    def deleteLast(self):
        temp=self.head 
        if temp is None:
            print("empty")
            return 
        if temp.next is None:
            temp=temp.next 
            return 
        while temp.next.next != None:
            temp=temp.next 
        temp.next=temp.next.next 
        
    def middleElement(self):
        slow=self.head 
        fast=self.head  
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next 
        print("middle element:",slow.data)
    def palidrome(self):
        temp=self.head 
        stack=[]


myList=LL()

first=Node(10)
second=Node(20)
third=Node(30)

myList.head=first 
first.next=second 
second.next=third 

myList.addFront(100)
myList.addLast(200)
myList.addLast(300)
myList.deleteFirst()
myList.deleteLast()
myList.print()
myList.middleElement()


    