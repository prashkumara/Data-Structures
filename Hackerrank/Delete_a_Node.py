def deleteNode(head, position):
    curr=head
    if position==0:
        head=curr.next
        return head
    i=0
    while curr.next!=None and i<position-1:
        curr=curr.next
        i+=1
    temp=curr.next
    curr.next=temp.next
    return head