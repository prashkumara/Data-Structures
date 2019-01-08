def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    count = 0
    curr = head

    while curr != None:
        count += 1
        curr = curr.next
    mid = int(math.ceil(count / 2))

    curr = head
    for i in range(mid):
        curr = curr.next
    return curr