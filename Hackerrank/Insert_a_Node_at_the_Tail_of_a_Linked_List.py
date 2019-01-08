def insertNodeAtTail(head, data):
    temp=head
    new_node=SinglyLinkedListNode(data)
    if temp==None:
        head=new_node
        return head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node
    return head 