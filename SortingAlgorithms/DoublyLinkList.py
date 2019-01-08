class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkList:
    def __init__(self):
        self.head=None

    # appending the data at the end of the list
    def appendNode(self,data):
        temp=self.head
        new_node=Node(data)

        if temp==None:
            self.head=new_node
            return

        while temp.next!=None:
            temp=temp.next

        new_node.prev=temp
        temp.next=new_node

    #appending the data at the beginning of the list
    def appendAtBeginning(self,data):
        temp=self.head
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return

        new_node.next=temp
        temp.prev=new_node
        self.head=new_node

    #deteting the Node at nth position
    def deleteNode(self,n):
        curr=self.head
        if n<1:
            print("no deletion possible")
            return
        if n==1:
            self.head=curr.next
            return
        else:
            i=1
            while(i<n-1 and curr!=None):
                i+=1
                curr=curr.next
        temp=curr.next
        curr.next=temp.next


    #display doubly linked list
    def display(self):
        lis=[]
        temp=self.head
        if temp==None:
            print("No list")
            return
        while temp!=None:
            lis.append(temp.data)
            temp=temp.next
        return(lis)

    #display doubly linked list in reverse order
    def revDisplay(self):
        lis = []
        temp = self.head
        if temp == None:
            print("No list")
            return
        while temp.next != None:
            temp = temp.next

        while temp!= None:
            lis.append(temp.data)
            temp = temp.prev
        return(lis)


mylist=DoublyLinkList()
mylist.appendNode(1)
mylist.appendNode(2)
mylist.appendAtBeginning(0)
mylist.appendAtBeginning(-1)
print("List" ,mylist.display())
print("Reverse List" ,mylist.revDisplay())
print("After deletion" ,mylist.deleteNode(1),mylist.display())

