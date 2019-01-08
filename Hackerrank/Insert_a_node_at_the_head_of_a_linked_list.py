def insertNodeAtHead(llist, data):
    temp = llist
    new_node = SinglyLinkedListNode(data)
    if temp == None:
        llist = new_node
        return llist
    llist = new_node
    new_node.next = temp
    return llist