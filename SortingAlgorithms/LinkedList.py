class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    #append at the end of the list
    def append(self,data):
        curr = self.head
        new_node=Node(data)

        if curr == None:
            self.head=new_node
            return

        while curr.next!=None:
            curr=curr.next

        curr.next = new_node

    #print linked list
    def display(self):
        lis=[]
        curr=self.head

        if curr == None:
            print('Empty list')
            return

        while curr!=None:
            lis.append(curr.data)
            curr=curr.next
        print(lis)

    #inserting a node at nth position
    def insertAtN(self,data,n):
        curr=self.head
        new_node = Node(data)
        i=0

        if n<1:
            print("Cannot be inserted in the list")
            return

        if n==1:
            new_node.next = self.head
            self.head=new_node
            return

        while curr!=None and i<n-2:
            print(i, curr.data)
            i+=1
            curr=curr.next

        new_node.next=curr.next
        curr.next=new_node

    #Delete a node at nth position
    def deleteNode(self,n):
        curr=self.head

        if curr==None:
            print("Emplty list, nothing to delete")
            return

        if n==1:
            self.head=curr.next
            return

        i=0
        while curr!=None and i<n-2:
            i+=1
            curr=curr.next

        temp=curr.next
        curr.next=temp.next

    def revlist(self,head):
        st = ""
        revlist = self.recPalindrome(head)
        return revlist
    def recPalindrome(self, head):
        if head == None:
            return ""
        else:
            return  self.recPalindrome (head.next)+str(head.data)

mylist =  LinkList()
mylist.insertAtN(2,1) #2
mylist.insertAtN(3,2) #2,3
mylist.insertAtN(4,1) #4,2,3
mylist.insertAtN(5,2) #4,5,2,3
mylist.append(2)        #4,5,2,3,2
mylist.display()
print(mylist.revlist(mylist.head))

