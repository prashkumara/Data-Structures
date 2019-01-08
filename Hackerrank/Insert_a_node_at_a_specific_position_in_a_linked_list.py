def insertNodeAtPosition(head, data, position):
    curr=head
    new_node=SinglyLinkedListNode(data)
    if position==1 or position==0:
        head=new_node
        new_node.next=curr
        return head
    i=0
    while curr.next!=None and i<position-1:
        curr=curr.next
        i+=1
    temp=curr.next
    curr.next=new_node
    new_node.next=temp
    return head