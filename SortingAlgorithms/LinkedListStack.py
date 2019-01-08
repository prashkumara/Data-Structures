class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedListWithStack:
    def __init__(self):
        self.head=None
    #push operation in stack with linkedlist
    def pushInStack(self,data):
        temp=self.head
        new_node=Node(data)
        if temp==None:
            self.head=new_node
            return
        new_node.next=temp
        self.head = new_node
        return

    # pop operation in stack with linkedlist
    def popInStack(self):
        temp=self.head
        if temp==None:
            print("Emptylist nothing to pop")
            return
        self.head=temp.next
        return

    #print the contents of the list
    def displayStack(self):
        lis=[]
        temp=self.head
        if temp==None:
            print("Empty list")
            return
        while temp!=None:
            lis.append(temp.data)
            temp=temp.next
        return lis

mylist=LinkedListWithStack()
mylist.popInStack()
mylist.pushInStack(4)
print(mylist.displayStack())
mylist.pushInStack(3)
print(mylist.displayStack())
mylist.pushInStack(2)
print(mylist.displayStack())
mylist.pushInStack(1)
print(mylist.displayStack())
mylist.popInStack()
print(mylist.displayStack())
mylist.popInStack()
print(mylist.displayStack())
mylist.popInStack()
print(mylist.displayStack())
mylist.popInStack()
print(mylist.displayStack())