def getNode(head, positionFromTail):
    lis = []
    curr = head

    while curr != None:
        lis.append(curr.data)
        curr = curr.next

    return lis[len(lis) - positionFromTail - 1]