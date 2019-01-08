class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:

    def __init__(self):
        self.head=None

    def appendInList(self,data):
        new_node=Node(data)
        temp=self.head

        if temp==None:
            self.head=new_node
            return

        while temp.next!=None:
            temp=temp.next

        temp.next=new_node

    def printList(self):
        lis=[]
        temp=self.head

        if temp==None:
            print("Empty list")
            return

        while(temp!=None):
            lis.append(temp.data)
            temp=temp.next
        return(lis)

    def reverseLinkList(self):

        curr_node = self.head
        prev_node = None
        #next_node=None

        if curr_node==None:
            print("Empty list")
            return

        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node

        self.head=prev_node





mylist = LinkList()

mylist.appendInList(1)
mylist.appendInList(2)
mylist.appendInList(3)
mylist.appendInList(4)
mylist.appendInList(5)
print("Actual List: ",mylist.printList())

mylist.reverseLinkList()
print("Reversed List",mylist.printList())