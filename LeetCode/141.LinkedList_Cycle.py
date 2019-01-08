def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    if head == None or head.next == None:
        return False

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        if fast == slow:
            return True
        else:
            slow = slow.next
            fast = fast.next.next
    return False